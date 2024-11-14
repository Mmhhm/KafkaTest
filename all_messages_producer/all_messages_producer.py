from kafka import KafkaProducer
import json


producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_emails(data):
    producer.send('all.messages', data)
    print('Producer sent full email successfully')

