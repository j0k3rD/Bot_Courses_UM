from flask import Blueprint, jsonify
from main.services import CourseService

topblue = Blueprint('topblue',__name__, url_prefix='/')

@topblue.route('/top/', methods=['GET'])
def top():
    course_service = CourseService()
    top_list = course_service.get_top_courses()
    if top_list == None:
        resp = jsonify({'status':'top_error'})
        resp.status_code = 404
    else:
        message = f'{top_list}'
        resp = jsonify({'status':'top_complete',
                    'message':message})
        resp.status_code = 200
    return resp