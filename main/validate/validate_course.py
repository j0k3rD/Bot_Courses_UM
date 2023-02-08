from main.services import CourseService

service = CourseService()

class CourseValidate():
    
    def validate_course(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_id(id):
                    return function(*args, **kwargs)
                return 'Course not found', 404
            return wrapper
        return decorator

    def get_course_by_url(self, course_url):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_course_by_url(course_url):
                    return function(*args, **kwargs)
                return f'Course not found by url, {course_url}', 404
            return wrapper
        return decorator