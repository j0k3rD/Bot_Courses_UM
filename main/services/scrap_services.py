from main.services.browser import Browser
from .browser_firefox import FirefoxBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from main.models import CourseModel
from ..import db
from flask import Blueprint, jsonify



class ScrapServices:

    def __init__(self, browser:Browser):
        self.browser = browser

    def search(self, keyword:str, url:str):
        html = self.browser.search(keyword, url)
        res = self.parser(html)
        courses = self.send_data(res)
        return courses
        

    def save_data(self, data:CourseModel):
        db.session.add(data)
        db.session.commit()

    #Mostrar al usuario los datos scrapeados
    def send_data(self, data):
        course_list = []
        for course in data:
            course_list.append(course)
        return course_list

        
    def parser(self, html:WebDriver):
        course_search = html.find_element(By.ID,
                                'courses_search')

        if course_search != None:
            list_courses = course_search.find_elements(By.CLASS_NAME,
                                'pointer')

            for card_course in list_courses:
                url_course = card_course.get_attribute('href')
                if url_course != None:
                    pass
                    # print("Curso", url_course)
                
                href = card_course.get_attribute("href")
                if href != None:
                    title = card_course.find_element(By.CLASS_NAME, "h5 no-margin bold inline-block".replace(" ", "."))
                    # print(title.text)
                    #Guardar en la base de datos
                    # data = CourseModel(url=href, title=title.text, count=0)
                    # course_repository = CourseRepository()
                    # course_repository.create(data)
                    data = title.text, url_course
                    return data