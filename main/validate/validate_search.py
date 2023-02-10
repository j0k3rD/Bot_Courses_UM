from main.services import SearchService

service = SearchService()

class SearchValidate():
    
    def validate_search(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_id(id):
                    return function(*args, **kwargs)
                return 'Search not found by id, {id}', 404
            return wrapper
        return decorator

    def get_by_user_id(self, user_id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_user_id(user_id):
                    return function(*args, **kwargs)
                return f'Search not found by user_id, {user_id}', 404
            return wrapper
        return decorator