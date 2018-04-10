from flask_restful import Resource
import config
import config.app_config as app_config
from flask import jsonify, request
from bson.objectid import ObjectId


class RoomList(Resource):
    def get(self):
        data = []
        db = config.mongoDBHelper(app_config.MONGODB_NAME)
        rooms = db.rooms.find({})
        for room in rooms:
            room['_id'] = str(room['_id'])
            data.append(room)
        resp = jsonify({'code': 0, 'message': 'success', 'data': data})
        return resp

    def post(self):
        content = request.get_json()

        if content is None:
            resp = jsonify({
                'code': 0,
                'message': 'Please check JSON format!',
                'data': ''
            })
            return resp
        else:
            room = {
                'name': content['name'],
                'room_type': content['room_type'],
                # TODO: put creator in this list
                'users': [],
                'room_no': 99,
                'user_count': 1,
                'black': '',
                'white': '',
                'status': '未开局'
            }

            db = config.mongoDBHelper(app_config.MONGODB_NAME)
            ret = db.rooms.insert(room)
            room['_id'] = str(ret)
            resp = jsonify({'code': 0, 'message': 'success', 'data': room})
            return resp


class Room(Resource):
    def get(self, room_id):
        data = []
        db = config.mongoDBHelper(app_config.MONGODB_NAME)
        room = db.rooms.find_one({'_id': ObjectId(room_id)})
        if room is not None:
            room['_id'] = str(room['_id'])
            data.append(room)
        resp = jsonify({'code': 0, 'message': 'success', 'data': data})
        return resp
