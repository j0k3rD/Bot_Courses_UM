from main.repositories import CourseRepository
from main.services.services import Service
from main.map import CourseSchema

repository = CourseRepository()
schema = CourseSchema()

class CourseService(Service):
    '''
    Clase que representa el servicio de la entidad Course

    param:
        - Service: Clase que hereda de la interfaz Service
    '''
    def add(self, model):
        return repository.create(model)
        
    def get_all(self):
        return repository.find_all()

    def get_by_id(self, id):
        return repository.find_by_id(id = id)

    def get_by_course_url(self, course_url):
        '''
        Método que obtiene un curso por su url

        param:
            - course_url: Url del curso
        '''
        return repository.find_course_by_url(course_url = course_url)

    def add_count(self, id):
        '''
        Método que agrega un conteo a un curso

        param:
            - id: Id del curso
        '''
        return repository.add_count(id = id)

    def get_top_courses(self):
        '''
        Método que obtiene los 10 cursos con más visitas

        return:
            - course_list: Lista de tuplas con el título y la url del curso
        '''
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