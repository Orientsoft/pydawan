from flask_restful import Resource


class RoomList(Resource):
    def get(self):
        return 'room_list'


class Room(Resource):
    def get(self, room_id):
        return 'room_id:' + room_id