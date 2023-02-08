from flask_restful import Resource
from flask import request
from main.services import CourseService, SearchService
from main.map import CourseSchema
from main.validate import CourseValidate

validate = CourseValidate()
schema = CourseSchema()
service = CourseService()

class Course(Resource):

    def get(self, id):
        
        @validate.validate_course(id)
        def validater():
            return schema.dump(service.get_by_id(id)), 201
        return validater()
            
    def delete(self, id):
        pass

    def put(self, id):
        pass


class Courses(Resource):

    def get(self):
        model = schema.dump(service.get_all(), many=True)
        return model, 201
        
    def post(self):

        courses_urls = request.json["courses"]
        discord_id = request.json["discord_id"]
        Search_service = SearchService()

        search_model = Search_service.get_by_user_id(user_id = discord_id)

        for i in range(len(courses_urls)):
            
            course = service.get_by_course_id(course_url = courses_urls[i][1])

            if course:
                service.add_count(id = course.id)
                return schema.dump(model), 201

            data = {
                "url": courses_urls[i][1],
                "title": courses_urls[i][0],
                "search_id": search_model.id
            }
            model = schema.load(data)
            return schema.dump(service.add(model)), 201