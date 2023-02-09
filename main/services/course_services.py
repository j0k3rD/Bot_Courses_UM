from main.repositories import CourseRepository
from main.services.services import Service
from main.map import CourseSchema


repository = CourseRepository()
schema = CourseSchema()


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

    def get_top_courses(self):
        schema_top_course = schema.dump(repository.find_top_courses(), many=True)
        course_list = []
        title_list = []
        for title in schema_top_course:
            title_list.append(title['title'])

        url_list = []
        for url in schema_top_course:
            url_list.append(url['url'])

        for i in range(10):
            course_list.append((title_list[i], url_list[i]))
        return course_list