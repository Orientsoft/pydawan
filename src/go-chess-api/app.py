from flask import Flask
from flask_restful import Api
from handlers.ping import Ping
from handlers.room import Room, RoomList
from handlers.user import User, UserList

app = Flask(__name__)

# Register api handlers here
api = Api(app)
api.add_resource(Ping, '/ping')
api.add_resource(RoomList, '/rooms')
api.add_resource(Room, '/rooms/<room_id>')
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)
