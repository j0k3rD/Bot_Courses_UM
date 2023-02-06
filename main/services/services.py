from abc import ABC, abstractmethod

class Service(ABC):
    
    @abstractmethod  
    def add(self, model):
        pass

    @abstractmethod    
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass