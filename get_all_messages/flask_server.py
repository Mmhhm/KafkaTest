from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

app = Flask(__name__)


@app.route('/api/email', methods=['POST'])
def get_emails():
    try:
        producer.send('all.messages', request.get_json())
        print(f'Producer sent full email successfully: {request.get_json()}')
        return jsonify({'message': 'OK'}), 200
    except Exception as e:
        print(f'Error occurred {e}')
        return jsonify({'message': 'Error'})


if __name__ == '__main__':
    app.run(debug=True)

# kafka-topics --describe --bootstrap-server localhost:9092 --topic all.messages



# kafka-console-consumer --topic all.messages --from-beginning --bootstrap-server localhost:9092







