from abc import ABC, abstractmethod

class Single(ABC):

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def put(self, id):
        pass

class Multiple(ABC):

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass