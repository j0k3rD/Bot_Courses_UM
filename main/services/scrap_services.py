from main.services.browser import Browser
from .browser_firefox import BrowserFirefox
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from main.models import CourseModel

class ScrapServices:

    def __init__(self, browser:Browser):
        self.browser = browser

    def search(self, keyword:str, url:str):
        html = self.browser.search(keyword, url)
        self.parser(html)

    def save_data(self, datalist):
        #TODO: guardar los 
        pass

    def parser(self, html:WebDriver):
        course_search = html.find_element(By.ID,
                                'courses_search')

        if course_search != None:
            list_courses = course_search.find_elements(By.CLASS_NAME,
                                'pointer')

            for card_course in list_courses:
                url_course = card_course.get_attribute('href')
                if url_course != None:
                    print("Curso", url_course)
                
                href = card_course.get_attribute("href")
                if href != None:
                    title = card_course.find_element(By.CLASS_NAME, "h5 no-margin bold inline-block".replace(" ", "."))
                    print(title.text)
