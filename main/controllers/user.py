from flask_restful import Resource
from flask import request
from main.services import UserService
from main.map import UserSchema
from main.validate import UserValidate

validate = UserValidate()
schema = UserSchema()
service = UserService()

class User(Resource):

    
    def get(self, id):

        @validate.validate_user(id)
        def validater():
            return schema.dump(service.get_by_id(id)), 201
        return validater()
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Users(Resource):

    def get(self):
        
        model = schema.dump(service.get_all(), many=True)
        return model, 201

    def post(self):

        # Json values.
        user_json = request.json
        discord_id = user_json["discord_id"]
        username = user_json["name"]

        @validate.get_user(discord_id = discord_id)
        def validater():
            return f"User already exists in database {discord_id} - {username}", 201
                        
        model = schema.load(request.json)
        return schema.dump(service.add(model)), 201