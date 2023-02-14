from main.services.browser import Browser
from .browser_firefox import FirefoxBrowser
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from main.models import SearchModel
from ..import db
from flask import Blueprint, jsonify
from main.constants import ScrapingServicesConstants as ScrapingConstants

class ScrapServices:
    '''
    Clase que representa el servicio de scraping (busqueda de cursos en la web)
    '''
    def __init__(self, browser:Browser):
        '''
        Constructor de la clase

        param:
            - browser: Navegador que se va a utilizar para realizar la búsqueda
        '''
        self.browser = browser

    def search(self, keyword:str, url:str):
        '''
        Funcion que realiza la busqueda de cursos en la web

        param:
            - keyword: Palabra clave a buscar
            - url: Url a la que se va a buscar
        '''
        html = self.browser.search(keyword, url)
        course = self.parser(html)
        res = self.send_data(course)
        html.close()
        return res

    #Mostrar al usuario los datos scrapeados
    def send_data(self, data):
        '''
        Funcion que muestra al usuario los datos scrapeados

        param:
            - data: Datos scrapeados
        '''
        if len(data) == 0:
            return None
        else:
            return data

    #Cerrar el navegador
    def close_browser(self):
        '''
        Funcion que cierra el navegador
        '''
        self.browser.close()

    def parser(self, html:WebDriver):
        '''
        Funcion que parsea la pagina web

        param:
            - html: Pagina web
        return:
            - course_list: Lista de cursos scrapeados
        '''
        title_course = html.find_elements(ScrapingConstants.SCRAP_METHOD_TITTLE , ScrapingConstants.SCRAP_TITTLE)
        title_course = [   title.text    for title in title_course]
        if title_course != None:
            pass
        url_courses = html.find_elements(ScrapingConstants.SCRAP_METHOD_URL , ScrapingConstants.SCRAP_URL)
        url_courses = [   url.get_attribute('href')    for url in url_courses]
        if url_courses != None:
            '''juntemos los dos'''
            course_list = []
            for i in range(len(title_course)):
                course_list.append((title_course[i],url_courses[i]))
            return course_list