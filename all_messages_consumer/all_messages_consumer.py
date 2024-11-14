print('Good by')
from kafka import KafkaConsumer, KafkaProducer
print('Good by')
import json
print('Good by 3')
from pymongo import MongoClient
print('Good by 4')
from stream_processor.stream_processor_service import find_hostile_words
print('Good by 5')
# from stream_processor.hostage import hostage_producer, producer as hp
# print('Good by 6')
# from stream_processor.explosive import explosive_producer, producer as ep

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092']
)
#
# explosive_producer = KafkaProducer(
#     bootstrap_servers=['localhost:9092']
# )

print('Hello')

client = MongoClient('mongodb://localhost:27017/')
db = client['hostile_messages']
all_messages_collection = db['all_messages']


# Kafka consumer setup
consumer = KafkaConsumer(
    'all.messages',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print('Established consumer')

for message in consumer:
    try:
        email = message.value
        all_messages_collection.insert_one(email)
        print(f'Consumed message {email}')

        hostile_sentences = find_hostile_words(email['sentences'])
        hostage_content = hostile_sentences['hostage_sentences']
        explosive_content = hostile_sentences['explosive_sentences']
        fully_hostile_content = hostile_sentences['fully_explosive']

        if hostile_sentences['is_hostile']:
            for s in hostage_content:
                producer.send('messages.hostage', s.encode('utf-8'))
                print('OK hostage')
            for s in explosive_content:
                producer.send('messages.explosive', s.encode('utf-8'))
                print('OK explosive')
            for s in fully_hostile_content:
                producer.send('messages.hostage', s.encode('utf-8'))
                producer.send('messages.explosive', s.encode('utf-8'))
    except Exception as e:
        print(f'Consumer did not receive the data: {e}')


# kafka-console-consumer --topic all.messages --from-beginning --bootstrap-server localhost:9092









