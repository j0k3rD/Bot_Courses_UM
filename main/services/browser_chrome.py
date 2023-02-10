from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from main.services.browser import Browser
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser(Browser):
    '''
    Clase que representa el navegador Chrome

    param:
        - Browser: Clase abstracta de busqueda
    '''

    def _get_service(self):
        service = Service()
        return service

    def _get_options(self):
        #Navegation Options
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        #options.add_argument('headless') #Comentar para ver como funciona
        return options

    def _get_browser(self):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self._get_options())
        return browser

    def search(self, keyword:str, url:str) -> WebDriver:
        #Open Browser
        driver=self._get_browser()
        driver.get(f'{url}={keyword}')
        return driver