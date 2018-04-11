from flask_restful import Resource
from flask import g


class Ping(Resource):
    def get(self):
        if hasattr(g, 'user_id'):
            return 'pong from user: ' + g.user_id
        else:
            return 'pong'
