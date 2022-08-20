from django_pika_pubsub import Producer


def produce_parse_task(key, body):
    producer = Producer.get_producer()
    producer.produce(
        body='{\'key\':\'' + key + '\', \'items\':\'' + body + '\'}',
        routing_key='parse_queue'
    )
