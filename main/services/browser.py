from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver


class Browser(ABC):
    '''
    Clase abstracta que define los métodos que deben implementar las clases que hereden de ella.
    '''
    @abstractmethod
    def _get_options(self):
        '''
        Método abstracto para obtener las opciones del navegador
        '''
        pass

    @abstractmethod
    def _get_service(self):
        '''
        Método abstracto para obtener el servicio del navegador
        '''
        pass

    @abstractmethod
    def _get_browser(self):
        '''
        Método abstracto para obtener el navegador
        '''
        pass

    @abstractmethod
    def search(self, keyword:str, url:str) -> WebDriver:
        '''
        Método abstracto para buscar en el navegador

        param:
            - keyword: Palabra clave a buscar
            - url: Url a la que se va a buscar
        return:
            - WebDriver: Navegador con la búsqueda realizada
        '''
        pass