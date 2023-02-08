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

        # Validate if user already exists.
        if service.get_by_discord_id(discord_id):
            return f'User already exists by discord_id, {discord_id}', 404
    
        # Create user.
        data = {
            "discord_id": discord_id,
            "name": username
        }
        model = schema.load(data)
        return schema.dump(service.add(model)), 201