from flask_restful import Resource
from main.services import UserService
from main.map import UserSchema

user_schema = UserSchema()
service = UserService()

class User(Resource):

    def get(self, id):
        return user_schema.dump(service.get_by_id(id)), 201
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Users(Resource):

    def get(self):
        pass

    def post(self):
        pass