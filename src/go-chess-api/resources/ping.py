from flask_restful import Resource
from flask import g


class Ping(Resource):
    def get(self):
        return 'pong from user: ' + g.user_id
