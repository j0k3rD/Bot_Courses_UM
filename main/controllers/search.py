from flask_restful import Resource
from flask import request
from main.services import SearchService
from main.map import SearchSchema
from main.validate import SearchValidate

validate = SearchValidate()
schema = SearchSchema()
service = SearchService()

class Search(Resource):

    def get(self, id):
        
        @validate.validate_search(id)
        def validate():
            return schema.dump(service.get_by_id(id)), 201
        return validate()
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Searchs(Resource):

    def get(self):
        model = schema.dump(service.get_all(), many=True)
        return model, 201

    def post(self):
        model = schema.load(request.get_json)
        return schema.dump(service.add(model)), 201