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