from flask_restful import Resource
from main.services import CourseService
from main.map import CourseSchema

course_schema = CourseSchema()
service = CourseService()

class Course(Resource):

    def get(self, id):
        return course_schema.dump(service.get_by_id(id)), 201
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Courses(Resource):

    def get(self):
        pass
        
    def post(self):
        pass