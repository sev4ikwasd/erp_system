import base64
import json
import pika
from django.core.management.base import BaseCommand
from xml.etree import cElementTree as ET
from data_handler.models import MeasureUnit, Product, Category
from erp_system import settings


def get_full_object_description(line, description):
    full_object_description = [None] * len(description)

    for i, field in enumerate(description):
        found_line = line.find(field)
        full_object_description[i] = None if found_line is None else found_line.text

    return full_object_description


def get_all_from_line_category(line):
    fields = ["Родитель", "Наименование"]
    full_object_description = get_full_object_description(line, fields)

    print(full_object_description)
    Category.objects.create(
        parent=full_object_description[0],
        name=full_object_description[1]
    )


def get_all_from_line_product(line):
    fields = ["Родитель", "Артикул", "Наименование", "Описание", "ТипНоменклатуры", "СтавкаНДС",
              "ЕдиницаХраненияОстатков", "ПометкаУдаления"]
    full_object_description = get_full_object_description(line, fields)

    Product.objects.create(
        category=full_object_description[0],
        code=full_object_description[1],
        name=full_object_description[2],
        description=full_object_description[3],
        product_type=full_object_description[4],
        rate_nds=full_object_description[5],
        measure_unit=full_object_description[6],
        hidden=full_object_description[7]
    )


def get_all_from_line_unit(line):
    fields = ["Наименование", "НаименованиеПолное"]
    full_object_description = get_full_object_description(line, fields)

    MeasureUnit.objects.create(
        name=full_object_description[0],
        full_name=full_object_description[1]
    )


root_tags = {
    "ГруппаНоменклатура": get_all_from_line_category,
    "ЕдиницыИзмерения": get_all_from_line_unit,
    "Номенклатура": get_all_from_line_product,
}


def callback(channel, method, properties, body):
    payload = json.loads(body)
    erp_key = payload.get('key')
    items = base64.b64decode(payload.get('items'))

    tree = ET.fromstring(items)

    for line in tree:
        tag_name = str(line.tag).replace('{http://www.agora.centrobit.ru}', '')
        root_tags[tag_name](line)


class Command(BaseCommand):
    help = 'Consumes parsing queue'

    def handle(self, *args, **options):
        credentials = pika.PlainCredentials(settings.RABBITMQ_USERNAME, settings.RABBITMQ_PASSWORD)
        parameters = pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=credentials,
        )
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='parse_queue', durable=True)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(
            queue='parse_queue',
            on_message_callback=callback,
        )
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
