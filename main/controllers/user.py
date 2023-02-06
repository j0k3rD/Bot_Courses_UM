from flask_restful import Resource
from flask import request
from main.services import UserService
from main.map import UserSchema
from .controller import Single, Multiple

schema = UserSchema()
service = UserService()

class User(Single, Resource):

    def get(self, id):
        return schema.dump(service.get_by_id(id)), 201
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Users(Multiple, Resource):

    def get(self):
        return schema.dump(service.get_all()), 201

    def post(self):
        model = schema.load(request.get_json())
        return schema.dump(service.add(model)), 201