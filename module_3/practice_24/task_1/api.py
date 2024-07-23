from flask import Flask, request, jsonify, abort
import pymongo
from bson import ObjectId


def connect_to_database():
    CONNECT_HOST = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(CONNECT_HOST)
    return client['fruits']


def convert_to_list(data):
    l = list()
    for i in data:
        i['_id'] = str(i['_id'])
        l.append(i)
    return l


api = Flask(__name__)
db = connect_to_database()


@api.route('/create_fruit', methods=['POST'])
def create_fruit():
    data = request.get_json()
    print(data)
    try:
        db.get_collection('fruits').insert_one({
            'name': data['name'],
            'price': data['price']
        })
        return jsonify({'status_code': 201})
    except:
        return abort(400)
    

@api.route('/get_all_fruits')
def get_all_fruit():
    data = convert_to_list(db.get_collection('fruits').find())
    return jsonify(data)
    

@api.route('/update_fruit', methods=['POST'])
def update_fruit():
    data = request.get_json()
    try:
        db.get_collection('fruits').update_one(
            {'_id': ObjectId(data['_id'])},
            {'$set': {'name': data['name'], 'price': data['price']}}
        )
        return jsonify({'status_code': 200})
    except:
        return abort(400)
    
    
@api.route('/delete_fruit', methods=['POST'])
def delete_fruit():
    data = request.get_json()
    try:
        db.get_collection('fruits').delete_one({
            '_id': ObjectId(data['_id'])
        })
        return jsonify({'status_code': 200})
    except:
        return abort(400)
    

@api.errorhandler(400)
def error_400():
    return jsonify({'status_code': 400})


if __name__ == '__main__':
    api.run(host='127.0.0.1', port='5000', debug=True)