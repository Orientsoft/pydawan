from flask_restful import Resource
import config
import config.app_config as app_config
from flask import jsonify
from bson.objectid import ObjectId


class UserList(Resource):
    def get(self):
        data = []
        db = config.mongoDBHelper(app_config.MONGODB_NAME)
        users = db.users.find({})
        for user in users:
            user['_id'] = str(user['_id'])
            data.append(user)
        resp = jsonify({'code': 0, 'message': 'success', 'data': data})
        return resp


class User(Resource):
    def get(self, user_id):
        data = []
        db = config.mongoDBHelper(app_config.MONGODB_NAME)
        user = db.users.find_one({'_id': ObjectId(user_id)})
        if user is not None:
            user['_id'] = str(user['_id'])
            data.append(user)
        resp = jsonify({'code': 0, 'message': 'success', 'data': data})
        return resp
