from main.services import UserService

service = UserService()

class ValidateUser():
    
    def validate_course(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_id(id):
                    return function(*args, **kwargs)
                return 'User not found', 404
            return wrapper
        return decorator