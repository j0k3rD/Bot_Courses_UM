from main.repositories.irepository import Create, Delete, Read, Update 
from .. import db

class SearchRepository(Create, Read, Delete):

    def create(self, model: db.Model):
        pass

    def delete(self, model: db.Model):
        pass 

    def delete_by_id(self, id: int):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id: int) -> db.Model:
        pass