import json
import logging

from confluent_kafka import Consumer

from settings import settings

log = logging.getLogger(__name__)


def mgs_kafka_json():
    consumer = Consumer({
        'bootstrap.servers': 'harmless-llama-10955-eu2-kafka.upstash.io:9092',
        'sasl.mechanism': 'SCRAM-SHA-256',
        'security.protocol': 'SASL_SSL',
        'sasl.username': settings.user_kafka,
        'sasl.password': settings.password_kafka,
        'group.id': 'YOUR_CONSUMER_GROUP',
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([settings.topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue

            if msg.error():
                log.error(f"Consumer error: {msg.error()}")
                continue
            print("Сообщения получено!")
            data = json.loads(msg.value().decode('utf-8'))
            return data
    finally:
        consumer.close()
