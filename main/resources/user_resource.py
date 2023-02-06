from flask import Blueprint, jsonify

scrapblue = Blueprint('scrapblue',__name__, url_prefix='/')

@scrapblue.route('/create', methods=['POST'])
def create_user():
    resp = jsonify({'status':'create_user'})
    resp.status_code = 200
    return resp

@scrapblue.route('/get', methods=['GET'])
def get_user():
    resp = jsonify({'status':'get_user'})
    resp.status_code = 200
    return resp