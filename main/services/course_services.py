from main.repositories import CourseRepository
from main.services.services import Service

repository = CourseRepository()

class CourseService(Service):

    def add(self, model):
        return repository.create(model)
        
    def get_all(self):
        return repository.find_all()

    def get_by_id(self, id):
        return repository.find_by_id(id = id)

    def get_by_course_url(self, course_url):
        return repository.find_course_by_url(course_url = course_url)

    def add_count(self, id):
        return repository.add_count(id = id)