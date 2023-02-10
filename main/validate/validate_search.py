from main.services import SearchService

service = SearchService()

class SearchValidate():
    '''
    Clase que valida los datos de la entidad Search
    '''

    def validate_search(self, id):
        '''
        Función que valida si la busqueda existe

        param:
            - id: id de la busqueda
        return:
            - Función: Si la busqueda existe
            - Error: Si la busqueda no existe
        '''
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_id(id):
                    return function(*args, **kwargs)
                return 'Search not found by id, {id}', 404
            return wrapper
        return decorator

    def get_by_user_id(self, user_id):
        '''
        Función que valida si la busqueda existe

        param:
            - user_id: id del usuario
        return:
            - Función: Si la busqueda existe
            - Error: Si la busqueda no existe
        '''
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_user_id(user_id):
                    return function(*args, **kwargs)
                return f'Search not found by user_id, {user_id}', 404
            return wrapper
        return decorator