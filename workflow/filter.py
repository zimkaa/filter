import json

from confluent_kafka import Consumer
from confluent_kafka import Producer

import config


def main():
    producer = Producer({'bootstrap.servers': config.HOST})

    consumer = Consumer({
        'bootstrap.servers': config.HOST,
        'group.id': 'listener_events',
        'auto.offset.reset': 'earliest',
    })

    consumer.subscribe(['events'])

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        data = msg.value().decode("utf-8")

        tikers = config.TIKERS.split(',')

        for tiker in tikers:
            if json.loads(data)['name'] == tiker:
                producer.produce('filtred', data.encode())
                producer.flush()


if __name__ == "__main__":
    main()
