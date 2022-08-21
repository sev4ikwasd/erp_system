import base64
import json
import uuid

import pika
from django.core.management.base import BaseCommand
from xml.etree import cElementTree as ET
from data_handler.models import MeasureUnit, Product, Category
from erp_system import settings


def get_full_object_description(line, description):
    # full_object_description = [None] * len(description)
    # for i, field in enumerate(description):
    #     print(i, field)
    #     found_line = line.find(field)
    #     full_object_description[i] = None if found_line is None else found_line.text

    full_object_description = []

    for element in line:
        if str(element.tag).replace('{http://www.agora.centrobit.ru}', '') in description:
            full_object_description.append(element.text)

    return full_object_description


def get_or_none(classmodel, **kwargs):
    obj = classmodel.objects.filter(**kwargs)
    return obj.first() if obj.count == 1 else None


def get_all_from_line_category(line):
    fields = ["Ссылка", "Родитель", "Наименование"]
    full_object_description = get_full_object_description(line, fields)

    Category.objects.create(
        link=uuid.UUID(full_object_description[0]),
        parent=get_or_none(Category, link=full_object_description[1]),
        name=full_object_description[2]
    )


def get_all_from_line_product(line):
    fields = ["Ссылка", "Родитель", "Артикул", "Наименование", "Описание", "ТипНоменклатуры", "СтавкаНДС",
              "ЕдиницаХраненияОстатков", "ПометкаУдаления"]
    full_object_description = get_full_object_description(line, fields)

    Product.objects.create(
        link=uuid.UUID(full_object_description[0]),
        category=get_or_none(Category, link=full_object_description[1]),
        code=full_object_description[2],
        name=full_object_description[3],
        description=full_object_description[4],
        product_type=Product.TYPES(full_object_description[5]),
        rate_nds=full_object_description[6],
        measure_unit=get_or_none(MeasureUnit, link=full_object_description[7]),
        hidden=full_object_description[7]
    )


def get_all_from_line_unit(line):
    fields = ["Ссылка", "Наименование", "НаименованиеПолное"]
    full_object_description = get_full_object_description(line, fields)

    MeasureUnit.objects.create(
        link=uuid.UUID(full_object_description[0]),
        name=full_object_description[1],
        full_name=full_object_description[2]
    )


root_tags = {
    "ГруппаНоменклатура": get_all_from_line_category,
    "ЕдиницыИзмерения": get_all_from_line_unit,
    "Номенклатура": get_all_from_line_product,
}


def callback(channel, method, properties, body):
    payload = json.loads(body)
    erp_key = payload.get('key')
    items = base64.b64decode(payload.get('items')).decode('utf-8')

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
