from confluent_kafka import Consumer
from confluent_kafka import Producer


host = 'localhost:9092'

producer = Producer({'bootstrap.servers': host})

consumer = Consumer({
    'bootstrap.servers': host,
    'group.id': 'listener',
    'auto.offset.reset': 'earliest',
})

consumer.subscribe(['registrations'])

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
