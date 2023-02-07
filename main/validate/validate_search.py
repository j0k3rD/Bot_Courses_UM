from main.services import SearchService

service = SearchService()

class SearchValidate():
    
    def validate_search(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_id(id):
                    return function(*args, **kwargs)
                return 'Search not found', 404
            return wrapper
        return decorator