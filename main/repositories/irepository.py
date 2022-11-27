from abc import ABC, abstractmethod
from ast import Pass
from .. import db

class Create(ABC):
    @abstractmethod  
    def create(self, model: db.Model):
        pass
        

class Read(ABC):
    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> db.Model:
        pass

class Update(ABC):
    @abstractmethod
    def update(self, model: db.Model) -> db.Model:
        pass

class Delete(ABC):
    @abstractmethod
    def delete(self, model: db.Model):
        pass 

    @abstractmethod
    def delete_by_id(self, id: int):
        pass