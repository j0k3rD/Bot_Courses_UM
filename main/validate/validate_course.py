from main.services import CourseService

service = CourseService()

class CourseValidate():
    '''
    Clase que valida los datos de la entidad Course
    '''
    
    def validate_course(self, id):
        '''
        Función que valida si el curso existe

        param:
            - id: id del curso
        return:
            - Función: Si el curso existe
            - Error: Si el curso no existe
        '''
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_id(id):
                    return function(*args, **kwargs)
                return 'Course not found', 404
            return wrapper
        return decorator

    def get_course_by_url(self, course_url):
        '''
        Función que valida si el curso existe

        param:
            - course_url: url del curso
        return:
            - Función: Si el curso existe
            - Error: Si el curso no existe
        '''
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_course_by_url(course_url):
                    return function(*args, **kwargs)
                return f'Course not found by url, {course_url}', 404
            return wrapper
        return decorator