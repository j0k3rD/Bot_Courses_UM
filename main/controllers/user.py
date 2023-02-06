from flask_restful import Resource
from flask import request
from main.services import UserService
from main.map import UserSchema
from main.models import UserService
from .. import db

user_schema = UserSchema()
service = UserService

class User(Resource):

    def get(self, id):
        return user_schema.dump(service.get_course(id)), 201
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Users(Resource):

    def get(self):
        pass
        
    def post(self):
        pass