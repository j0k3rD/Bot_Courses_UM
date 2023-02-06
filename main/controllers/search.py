from flask_restful import Resource
from main.services import SearchService
from main.map import SearchSchema

search_schema = SearchSchema()
service = SearchService()

class Search(Resource):

    def get(self, id):
        return search_schema.dump(service.get_by_id(id)), 201
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Search(Resource):

    def get(self):
        pass

    def post(self):
        pass