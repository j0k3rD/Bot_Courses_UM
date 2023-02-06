from main.repositories import SearchRepository
from main.services.services import Service

repository = SearchRepository()

class SearchService(Service):

    def add(self, model):
        return repository.create(model)
        
    def get_all(self):
        return repository.find_all()

    def get_by_id(self, id):
        return repository.find_by_id(id = id)