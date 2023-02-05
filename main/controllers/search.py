from flask_restful import Resource
from flask import request
from main.services import SearchService
from main.models import SearchModel
from .. import db

search_schema = SearchSchema()
service = SearchService

class Search(Resource):

    def get(self, id):
        search = db.session.query(SearchModel).get_or_404(id)
        return search_schema.dump(search), 201
            
    def delete(self, id):
        search = db.session.query(SearchModel).get_or_404(id)
        try:
            db.session.delete(search)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        search = db.session.query(SearchModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(search, key, value)
        try:
            db.session.add(search)
            db.session.commit()
            return search_schema.dump(search), 201
        except:
            return '', 404


class Search(Resource):

    def get(self):
        return search_schema.dump(service.get_courses(), many=True)
        
    def post(self):
        course = search_schema.load(request.get_json())
        db.session.add(course)
        db.session.commit()
        return search_schema.dump(course), 201