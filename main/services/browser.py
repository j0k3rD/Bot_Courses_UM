from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver

class Browser(ABC):

    @abstractmethod
    def __get_options(self):
        pass

    @abstractmethod
    def __get_service(self):
        pass

    @abstractmethod
    def __get_browser(self):
        pass

    @abstractmethod
    def search(self, keyword:str, url:str) -> WebDriver:
        pass


        
