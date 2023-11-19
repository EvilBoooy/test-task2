from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://db:27017/')
db = client.mydatabase


@app.route('/', methods=['GET'])
def get_values():
    values = db.values.find()
    return {'values': [value['value'] for value in values]}


@app.route('/', methods=['POST'])
def create_value():
    if request.method == 'POST':
        key = request.json['key']
        value = request.json['value']
        db.values.insert_one({'key': key, 'value': value})
        return {'message': 'Value created'}
    else:
        return {'error': 'Method not allowed'}, 405


@app.route('/<key>', methods=['GET'])
def get_value(key):
    value = db.values.find_one({'key': key})
    if value:
        return {'value': value['value']}
    else:
        return {'error': 'Value not found'}, 404


@app.route('/<key>', methods=['PUT'])
def update_value(key):
    if request.method == 'PUT':
        new_value = request.json['value']
        db.values.update_one({'key': key}, {'$set': {'value': new_value}})
        return {'message': 'Value updated'}
    else:
        return {'error': 'Method not allowed'}, 405


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
