from flask import Blueprint, jsonify
from main.services import ScrapServices, FirefoxBrowser, ChromeBrowser


scrapblue = Blueprint('scrapblue',__name__, url_prefix='/')

@scrapblue.route('/search/<browser>/<keyword>/', methods=['GET'])
def search(browser:str,keyword:str):
    if browser.lower() != "chrome" and browser.lower() != "firefox":
        resp = jsonify({'status':'Invalid browser option! (Choose between "chrome" or "firefox")'})
        resp.status_code = 404
    else:
        if browser.lower() == "firefox":
            browser_web = FirefoxBrowser()
        else:
            browser_web = ChromeBrowser()
            
        scrap_service = ScrapServices(browser_web)
        courses = scrap_service.search(keyword, "https://codigofacilito.com/search?utf8=✓&keyword")
        message = f"Encontre unos Cursos sobre **{keyword}** justo para vos!: \n1- *{courses[0]}* \n2- *{courses[1] }* \n3- *{courses[2]}*"
        resp = jsonify({'status':'search_complete',
                        'message':message})
        resp.status_code = 200
            
    return resp