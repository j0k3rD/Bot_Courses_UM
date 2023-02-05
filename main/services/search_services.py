from .. import db
from main.models import SearchModel
from main.map import SearchSchema
from .command import Command, Task
from flask import request

search_schema = SearchSchema()

class SearchService:

    def add_search(self):
        search = search_schema.load(request.get_json())
        if self.register_search(search):
            db.session.add(search)
            db.session.commit()
            return search
        return False  

    def get_searches(self):
        course = db.session.query(SearchModel).all()
        return course

    def register_search(self, search):
        task = Task()
        task.execute(search)

    
class SaveSearch(Command):

    def execute(self, course):
        try:
            db.session.add(course)
            db.session.commit()
            return course.to_json(), 201
        except:
            return '', 404