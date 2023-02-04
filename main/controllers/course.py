from flask_restful import Resource
from flask import request
from main.services import CourseService
from main.map import CourseSchema
from ..repositories import CourseRepository
from main.models import CourseModel
from .. import db

course_schema = CourseSchema()
course_repository = CourseRepository()
service = CourseService

class Course(Resource):

    def get(self, id):
        course = db.session.query(CourseModel).get_or_404(id)
        return course_schema.dump(course), 201
            
    def delete(self, id):
        course = db.session.query(CourseModel).get_or_404(id)
        try:
            db.session.delete(course)
            db.session.commit()
            return '', 204
        except:
            return '', 404

    def put(self, id):
        course = db.session.query(CourseModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(course, key, value)
        try:
            db.session.add(course)
            db.session.commit()
            return course_schema.dump(course), 201
        except:
            return '', 404


class Courses(Resource):

    def get(self):
        return course_schema.dump(service.get_courses(), many=True)
        
    def post(self):
        course = course_schema.load(request.get_json())
        db.session.add(course)
        db.session.commit()
        return course_schema.dump(course), 201