from main.services import UserService

service = UserService()

class UserValidate():
    
    def validate_user(self, id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_id(id):
                    return function(*args, **kwargs)
                return 'User not found', 404
            return wrapper
        return decorator

    def get_user(self, discord_id):
        def decorator(function):
            def wrapper(*args, **kwargs):
                if service.get_by_discord_id(discord_id):
                    return function(*args, **kwargs)
                return f'User not found by discord_id, {discord_id}', 404
            return wrapper
        return decorator