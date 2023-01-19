from main.services.browser import Browser
from .browser_firefox import FirefoxBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from main.models import CourseModel
from ..import db
from flask import Blueprint, jsonify
from ..repositories.course_repository import CourseRepository
from ..map.course_schema import CourseSchema

course_repository = CourseRepository()
course_schema = CourseSchema()


class ScrapServices:

    def __init__(self, browser:Browser):
        self.browser = browser
        self.course_list = []

    def search(self, keyword:str, url:str):
        html = self.browser.search(keyword, url)
        course = self.parser(html)
        res = self.send_data(course)
        return res
        
    def save_data(self, data:CourseModel):
        db.session.add(data)
        db.session.commit()

    #Mostrar al usuario los datos scrapeados
    def send_data(self, data):
        return data[0], data[1], data[2], data[3]
        
    def parser(self, html:WebDriver):
        title_course = html.find_elements("xpath","//h2[@class='no-margin-bottom normal-line-height f-text-22 ibm bold-600 f-top-12']")
        # title_courses = [   title.text    for title in title_courses]

        url_courses = html.find_elements("xpath","//h2[@class='no-margin-bottom normal-line-height f-text-22 ibm bold-600 f-top-12']//a[1]")
        url_courses = [   url.get_attribute('href')    for url in url_courses]

        '''para cada titulo su respectiva url y guardar en lista'''
        for title, url in zip(title_course, url_courses):
            data = title.text, url
            self.course_list.append(data)
        return self.course_list