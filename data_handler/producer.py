import base64

import pika

from erp_system import settings


def produce_parse_task(key, body):
    producer = Producer.get_producer()
    producer.produce(
        body='{\"key\":\"' + key + '\", \"items\":\"' + str(base64.b64encode(body.encode('utf-8')), 'utf-8') + '\"}',
        routing_key='parse_queue'
    )


class Producer:
    def __init__(self):
        credentials = pika.PlainCredentials(settings.RABBITMQ_USERNAME, settings.RABBITMQ_PASSWORD)
        self.parameters = pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            credentials=credentials,
        )
        self.exchanges = []

    def produce(self, body, routing_key):
        exchange = ''
        queue = routing_key
        connection = pika.BlockingConnection(self.parameters)
        channel = connection.channel()
        channel.queue_declare(queue=queue, durable=True)
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        connection.close()

    @classmethod
    def get_producer(cls):
        return cls()
