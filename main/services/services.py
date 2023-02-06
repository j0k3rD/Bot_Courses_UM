from abc import ABC, abstractmethod

class Service(ABC):
    
    @abstractmethod  
    def add_course(self, course):
        pass

    @abstractmethod    
    def get_courses(self):
        pass

    @abstractmethod  
    def obtener_cuota(self, id):
        pass