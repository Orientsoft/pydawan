from flask_restful import Resource


class UserList(Resource):
    def get(self):
        return 'room_list'


class User(Resource):
    def get(self, user_id):
        return 'user_id:' + user_id