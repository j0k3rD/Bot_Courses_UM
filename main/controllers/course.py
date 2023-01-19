from flask_restful import Resource
from flask import request
from main.services import ScrapServices
from main.map import CourseSchema
from ..repositories import CourseRepository
from main.models import CourseModel
from ..import db

course_schema = CourseSchema()
course_repository = CourseRepository()

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
        courses = db.session.query(CourseModel)
        
    def post(self):
        services = ScrapServices()
        course = course_schema.load(request.get_json())
        return services.save_data(course)