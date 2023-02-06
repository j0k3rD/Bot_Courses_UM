from flask_restful import Resource
from flask import request
from main.services import CourseService
from ..repositories import SearchRepository
from main.map import CourseSchema
from .. import db

course_schema = CourseSchema()
course_repository = SearchRepository()
service = CourseService

class Course(Resource):

    def get(self, id):
        return course_schema.dump(service.get_course(id)), 201
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Courses(Resource):

    def get(self):
        pass
        
    def post(self):
        pass