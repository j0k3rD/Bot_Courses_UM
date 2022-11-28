from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from main.services.browser import Browser
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser(Browser):

    def _Browser__get_service(self):
        service = Service()
        return service

    def _Browser__get_options(self):
        #Navegation Options
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        #options.add_argument('headless') #Comentar para ver como funciona
        return options

    def _Browser__get_browser(self):
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self._Browser__get_options())
        return browser

    def search(self, keyword:str, url:str) -> WebDriver:
        #Open Browser
        driver=self._Browser__get_browser()
        driver.get(f'{url}={keyword}')
        return driver