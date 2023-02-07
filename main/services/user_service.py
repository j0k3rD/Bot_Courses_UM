from main.repositories import UserRepository
from main.services.services import Service

repository = UserRepository()

class UserService(Service):

    def add(self, model):
        return repository.create(model)
        
    def get_all(self):
        return repository.find_all()

    def get_by_id(self, id):
        return repository.find_by_id(id = id)

    def get_by_discord_id(self, discord_id):
        return repository.find_by_discord_id(discord_id = discord_id)