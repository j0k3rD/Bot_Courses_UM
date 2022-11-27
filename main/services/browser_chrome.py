from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from main.services.browser import Browser
from webdriver_manager.chrome import ChromeDriverManager
class ChromeBrowser(Browser):

    def __get_service(self):
        service = Service()
        return service

    def __get_options(self):
        #Navegation Options
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        #options.add_argument('headless');
        #options.add_argument('window-size=0x0') ##Comentar para ver como funciona
        return options

    def __get_browser(self):
        # driver_path = "/usr/bin/chromedriver"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.__get_options())
        return driver

    def search(self, keyword:str, url:str) -> WebDriver:
        #Open Browser
        driver=self.__get_browser()
        driver.get(f'{url}={keyword}')
        return driver