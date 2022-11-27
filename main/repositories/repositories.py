from abc import ABC, abstractmethod

class Repository(ABC):
    
    """ deprecated
Repository class viola el principio de segregacion de interfaces,
ver irepository.py  
"""

    @abstractmethod
    def create(self):
        pass
    
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self):
        pass