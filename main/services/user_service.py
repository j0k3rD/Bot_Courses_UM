from main.repositories import UserRepository
from main.services.services import Service

repository = UserRepository

class UserService(Service):

    def add_user(self, course):
        return repository.create(course)
        
    def get_users(self):
        return repository.find_all()

    def get_user(self, id):
        return repository.find_by_id(id = id)