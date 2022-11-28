from flask import Blueprint, jsonify


home = Blueprint('home',__name__, url_prefix='/')

@home.route('/', methods=['GET'])
def index():
    resp = jsonify({'project':'Bot_discord'})
    resp.status_code = 200
    return resp

@home.route('/healthcheck')
def heal_check():
    return jsonify({'status': 'up'}), 200