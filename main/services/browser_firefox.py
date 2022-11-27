from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
import os
from main.services.browser import Browser 

class FirefoxBrowser(Browser):
    def __get_service(self):
        service = Service()
        return service

    def __get_options(self):
        options = webdriver.FirefoxOptions()
        #options.headless = True
        options.set_preference("browser.cache.disk.enable", False)
        options.set_preference("browser.cache.memory.enable", False)
        options.set_preference("browser.cache.offline.enable", False)
        options.set_preference("network.http.use-cache", False)
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.log.level = "INFO"
        return options

    def __get_browser(self):
        browser = webdriver.Firefox(options=self.__get_options(), service=self.__get_service())
        #browser.set_window_position(0, 0)
        return browser

    def search(self, keyword:str, url:str) -> WebDriver:
        #TODO: buscar en el sitio codigofacilito devoler html 
        #Open Browser
        driver = self.__get_browser()
        driver.get(f'{url}={keyword}')
        return driver