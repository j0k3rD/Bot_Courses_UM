from flask_restful import Resource
from flask import request
from main.services import SearchService, UserService
from main.map import SearchSchema, UserSchema
from main.validate import SearchValidate, UserValidate

validate = SearchValidate()
schema = SearchSchema()
service = SearchService()

class Search(Resource):

    def get(self, id):
        
        @validate.validate_search(id)
        def validater():
            return schema.dump(service.get_by_id(id)), 201
        return validater()
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Searchs(Resource):

    def get(self):
        
        model = schema.dump(service.get_all(), many=True)
        return model, 201

    def post(self):

        user_validate = UserValidate()
        user_service = UserService()
        user_schema = UserSchema()

        # Json values
        user_json = request.json
        keywords = user_json["keywords"]
        discord_id = user_json["discord_id"]

        @user_validate.get_user(discord_id = discord_id)
        def validater():

            user = user_schema.dump(user_service.get_by_discord_id(discord_id = discord_id))
            data = {
                "keywords": keywords,
                "user_id": user["id"]
            }
            model = schema.load(data) 
            return schema.dump(service.add(model)), 201

        return validater()

        