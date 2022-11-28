from flask_restful import Resource
from flask import request
from main.services import ScrapServices
from ..repositories import CourseRepository

service_scrap = ScrapServices()

class Course(Resource):
    def get(self):
        return CourseRepository().find_all()
    
    def post(self):
        data = request.get_json()
        service_scrap.search(data['keyword'], data['url'])
        return {'status':'search_complete'}, 200
            