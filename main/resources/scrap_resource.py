from flask import Blueprint, jsonify
from main.services import ScrapServices, FirefoxBrowser, ChromeBrowser
from main.constants import ScrapingResourcesConstants as ScrapingConstants
import urllib.parse

scrapblue = Blueprint('scrapblue',__name__, url_prefix='/')

@scrapblue.route('/search/<browser>/<keyword>/', methods=['GET'])
def search(browser:str,keyword:str):
    '''
    Funcion llamada por request GET a la ruta /api/v1/search/<browser>/<keyword>/

    args:
        - browser: Indica el navegador a utilizar para la busqueda
        - keyword: Indica la palabra clave a buscar
    return:
        - resp: Devuelve el listado de cursos
    '''
    browser = browser.lower()
    
    if browser != "chrome" and browser != "firefox":
        resp = jsonify({'status':ScrapingConstants.BROWSER_ERROR})
        resp.status_code = 404
    else:
        if browser == "firefox":
            browser_web = FirefoxBrowser()
        else:
            browser_web = ChromeBrowser()
            
        scrap_service = ScrapServices(browser_web)
        courses = scrap_service.search(urllib.parse.quote(keyword), ScrapingConstants.URL)
        if courses == None:
            resp = jsonify({'status':ScrapingConstants.SEARCH_ERROR})
            resp.status_code = 404
        else:
            message = f'{courses}'
            resp = jsonify({'status':ScrapingConstants.SEARCH_COMPLETE,
                        'message':message})
            resp.status_code = 200
    return resp 