from flask import Blueprint, jsonify
from main.services import ScrapServices, FirefoxBrowser, ChromeBrowser
import urllib.parse


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
        courses = scrap_service.search(urllib.parse.quote(keyword), "https://codigofacilito.com/courses?utf8=✓&search[keyword]")
        if courses == None:
            resp = jsonify({'status':'search_error'})
            resp.status_code = 404
        else:
            message = f'{courses}'
            resp = jsonify({'status':'search_complete',
                        'message':message})
            resp.status_code = 200
    return resp 