from flask_restful import Resource
from flask import request
from main.services import CourseService, SearchService, UserService
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

        json = request.json

        if not json:
            return "No json data", 400

        elif "top_courses" in json:
            return self.post_top_courses(limit = request.json["top_courses"])

        elif "courses" and "discord_id" in json:
            return self.post_course(courses_urls = request.json["courses"], discord_id = request.json["discord_id"])

        else:
            return "Incorrect json data", 400
            

    def post_course(self, courses_urls, discord_id):

        Search_service = SearchService()
        User_service = UserService()

        user_model = User_service.get_by_discord_id(discord_id = discord_id)

        search_model = Search_service.get_by_user_id(user_id = user_model.id)
        search_id = search_model.id

        for i in range(len(courses_urls)):
            course = service.get_by_course_url(course_url = courses_urls[i][1])

            if course:
                service.add_count(id = course.id)
                if (i == len(courses_urls) - 1):
                    return "All course models saved", 201
                continue
            
            data = {
                "url": courses_urls[i][1],
                "title": courses_urls[i][0],
                "search_id": search_id
            }

            model = schema.load(data)
            model = service.add(model)
            
            if (i == len(courses_urls) - 1):
                return "All course models saved", 201

    def post_top_courses(self, limit):
        schema_top_course = schema.dump(service.get_top_courses(limit), many=True)
        # print(schema_top_course)
        course_list = []
        title_list = []
        # for title in schema_top_course:
        #     title_list.append(title['title'])

        url_list = []
        # for url in schema_top_course:
        #     url_list.append(url['url'])

        # for i in range(limit):
        #     course_list.append((title_list[i], url_list[i]))
        #     print(course_list)
        # return course_list
        for item in schema_top_course:
            for title in item('title'):
                title_list.append(title)
            for url in item('url'):
                url_list.append(url)
        for i in range(limit):
            course_list.append((title_list[i], url_list[i]))
        print(course_list)
        return course_list

