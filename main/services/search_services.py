from main.repositories import SearchRepository
from main.services.services import Service

repository = SearchRepository

class SearchService(Service):

    def add_search(self, course):
        return repository.create(course)
        
    def get_searches(self):
        return repository.find_all()

    def get_search(self, id):
        return repository.find_by_id(id = id)