from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  #Espera a que el HTML deje de cargar para realizar las operaciones
from selenium.webdriver.support import expected_conditions as EC #Para añadir condiciones de busqueda
from selenium.webdriver.common.by import By #Ayuda a configurar esas busquedas
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webdriver import WebDriver
#import pandas as pd

#User search variable
#to_search = "javascript"

class ScrapServices:

    # def __get_service(self):
    #     return driver_path

    def __get_options(self):
        #Navegation Options
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
        browser = webdriver.Firefox(options=self._Browser__get_options(), service=self._Browser__get_service())
        #browser.set_window_position(0, 0)
        return browser

    def search(self, keyword:str, html:WebDriver):

        course_search = html.find_element(By.CLASS_NAME,
                                'courses-main-area relative'.replace(" ", "."))

        if course_search != None:
            list_courses = course_search.find_elements(By.CLASS_NAME,
                                'f-border f-border--light f-card-reveal f-card-reveal--active f-course-horizontal flex-block medium-radius overflow-hidden')

            for card_course in list_courses:
                url_course = card_course.get_attribute("href")
                if url_course != None:
                    pass
                
                href = card_course.get_attribute("href")
                if href != None:
                    title = card_course.find_element(By.CLASS_NAME, "no-margin-bottom normal-line-height f-text-22 ibm bold-600 f-top-12".replace(" ", "."))
                    data = title.text, url_course
                    print(data)

a = ScrapServices()
a.search("python", html=WebDriver)