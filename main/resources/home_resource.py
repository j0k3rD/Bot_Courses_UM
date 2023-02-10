from flask import Blueprint, jsonify

home = Blueprint('home',__name__, url_prefix='/')

@home.route('/', methods=['GET'])
def index():
    '''
    Funcion llamada por request GET a la ruta /api/v1/

    return:
        - json: Devuelve un json con el nombre del proyecto
    '''
    resp = jsonify({'project':'Bot_discord'})
    resp.status_code = 200
    return resp

@home.route('/healthcheck', methods=['GET'])
def heal_check():
    '''
    Funcion llamada por request GET a la ruta /api/v1/healthcheck

    return:
        - json: Devuelve un json con el estado del server (api)
    '''
    return jsonify({'status': 'up'}), 200