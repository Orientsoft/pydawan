from flask_restful import Resource
import config
import config.app_config as app_config
from flask import jsonify


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
        return 'room_id:' + room_id