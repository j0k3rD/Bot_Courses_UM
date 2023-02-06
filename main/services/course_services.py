from main.repositories import CourseRepository
from main.services.services import Service

repository = CourseRepository

class CourseService(Service):

    def add_course(self, course):
        return repository.create(course)
        
    def get_courses(self):
        return repository.find_all()

    def get_course(self, id):
        return repository.find_by_id(id = id)