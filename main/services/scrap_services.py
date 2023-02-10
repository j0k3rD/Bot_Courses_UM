from main.services.browser import Browser
from .browser_firefox import FirefoxBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from main.models import SearchModel
from ..import db
from flask import Blueprint, jsonify

class ScrapServices:

    def __init__(self, browser:Browser):
        self.browser = browser

    def search(self, keyword:str, url:str):
        html = self.browser.search(keyword, url)
        course = self.parser(html)
        res = self.send_data(course)
        html.close()
        return res

    #Mostrar al usuario los datos scrapeados
    def send_data(self, data):
        if len(data) == 0:
            return None
        else:
            return data

    #Cerrar el navegador
    def close_browser(self):
        self.browser.close()

    def parser(self, html:WebDriver):
        title_course = html.find_elements("xpath","//h2[@class='no-margin-bottom normal-line-height f-text-22 ibm bold-600 f-top-12']")
        title_course = [   title.text    for title in title_course]
        if title_course != None:
            pass
        url_courses = html.find_elements("xpath","//h2[@class='no-margin-bottom normal-line-height f-text-22 ibm bold-600 f-top-12']//a[1]")
        url_courses = [   url.get_attribute('href')    for url in url_courses]
        if url_courses != None:
            '''juntemos los dos'''
            course_list = []
            for i in range(len(title_course)):
                course_list.append((title_course[i],url_courses[i]))
            return course_list