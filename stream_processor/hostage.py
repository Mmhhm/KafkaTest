from kafka import KafkaProducer, KafkaConsumer
import json
from postgres.db import Hostages, session


consumer = KafkaConsumer(
    'messages.hostage',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
)

for m in consumer:
    message = m.value.decode("utf-8")
    hostage = Hostages(
        sentence=message
    )
    session.add(hostage)
    session.commit()
    print(f'Explosive consumer received message successfully {message}')

