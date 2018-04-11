import jwt
from flask import Flask, request, abort, g
from flask_restful import Api
from resources.ping import Ping
from resources.room import Room, RoomList
from resources.user import User, UserList
import config.app_config as app_config

app = Flask(__name__)

# Register api resources here
api = Api(app)
api.add_resource(Ping, '/ping')
api.add_resource(RoomList, '/rooms')
api.add_resource(Room, '/rooms/<room_id>')
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')

# @app.before_request
# def pre_auth():
#     if 'Authorization' in request.headers:
#         auth_jwt = request.headers['Authorization']
#         if auth_jwt != '':
#             payload = jwt.decode(
#                 auth_jwt, app_config.JWT_SECRET, algorithms=['HS256'])
#             # Store user id in g
#             g.user_id = payload['user_id']
#         else:
#             abort(403)
#     else:
#         abort(403)

if __name__ == '__main__':
    app.run(debug=True)
