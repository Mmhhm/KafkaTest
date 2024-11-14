from kafka import KafkaProducer, KafkaConsumer
import json
from postgres.db import Explosives, session, conn


consumer = KafkaConsumer(
    'messages.explosive',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
)

for m in consumer:
    message = m.value.decode("utf-8")
    explosion = Explosives(
        sentence=message
    )
    session.add(explosion)
    session.commit()
    print(f'Explosive consumer received message successfully {message}')
