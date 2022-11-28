from .. import db
from main.models import CourseModel
from main.map import CourseSchema
from .command import Command, Task
from flask import request


course_schema = CourseSchema()


class CourseService:

    def add_course(self):
        course = course_schema.load(request.get_json())
        if self.register_course(course):
            db.session.add(course)
            db.session.commit()
            print('Return course')
            return course
        return False  

    def get_courses(self):
        course = db.session.query(CourseModel).all()
        return course

    def register_course(self, course):
        task = Task()
        task.execute(course)

    
class SaveCourse(Command):

    def execute(self, course):
        try:
            db.session.add(course)
            db.session.commit()
            return course.to_json(), 201
        except:
            return '', 404