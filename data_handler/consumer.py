from django_pika_pubsub import MyConsumer
import json
from xml.etree import cElementTree as ET
from models import MeasureUnit, Product, Category


def get_full_object_description(line, description):
    full_object_description = [None] * len(description)

    for i, field in enumerate(description):
        found_line = line.find(field)
        full_object_description[i] = None if found_line is None else found_line.text

    return full_object_description


def get_all_from_line_category(line):
    fields = ["Родитель", "Наименование"]
    full_object_description = get_full_object_description(line, fields)

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
    items = payload.get('items')

    tree = ET.fromstring(items)

    for line in tree:
        tag_name = str(line.tag).replace('{http://www.agora.centrobit.ru}', '')
        root_tags[tag_name](line)


consumer = MyConsumer.get_consumer()
consumer.consume(
    routing_key='parse_queue',
    callback=callback,
)
