from confluent_kafka import Consumer
from confluent_kafka import Producer

import config


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
    new_data = f"New {data}"

    producer.produce('filtred', new_data.encode())
    producer.flush()
    print(f'Received message: {msg.value().decode("utf-8")}')

consumer.close()
