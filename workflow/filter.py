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
            try:
                my_filter = json.loads(data)[tiker]
                write_data = {tiker: my_filter}
                producer.produce('filtred', json.dumps(write_data).encode())
                producer.flush()
            except KeyError:
                print("No ticker in data")
                continue


if __name__ == "__main__":
    main()
