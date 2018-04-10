from flask_restful import Resource
import config
import config.app_config as app_config
from flask import jsonify
from bson.objectid import ObjectId


class RoomList(Resource):
    def get(self):
        data = []
        db = config.mongoDBHelper(app_config.MONGODB_NAME)
        rooms = db.rooms.find({})
        for room in rooms:
            room['_id'] = str(room['_id'])
            data.append(room)
        resp = jsonify({"code": 0, "message": "success", "data": data})
        return resp


class Room(Resource):
    def get(self, room_id):
        data = []
        db = config.mongoDBHelper(app_config.MONGODB_NAME)
        room = db.rooms.find_one({"_id": ObjectId(room_id)})
        if room is not None:
            room['_id'] = str(room['_id'])
            data.append(room)
        resp = jsonify({"code": 0, "message": "success", "data": data})
        return resp
