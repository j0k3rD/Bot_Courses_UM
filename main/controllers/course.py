from flask_restful import Resource
from flask import request
from main.services import CourseService, SearchService, UserService
from main.map import CourseSchema
from main.validate import CourseValidate, SearchValidate, UserValidate


class Course(Resource):
    '''
    Clase que representa el controlador de la entidad Course

    param: 
        - Resource: Clase de la cual hereda
    '''

    def __init__(self):
        self.__validate = CourseValidate()
        self.__schema = CourseSchema()
        self.__service = CourseService()


    def get(self, id):
        '''
        Función que obtiene un curso por su id

        args:
            - id: id del curso
        return:
            - Curso en formato json o error 404
        '''
        @self.__validate.validate_course(id)
        def validater():
            return self.__schema.dump(self.__service.get_by_id(id)), 201
        return validater()

    '''
    TODO: Implementar delete y put en caso de agregar administrador.     
    def delete(self, id):
        pass

    def put(self, id):
        pass
    '''


class Courses(Resource):
    '''
    Clase que representa el controlador de la entidad Courses

    param:
        - Resource: Clase de la cual hereda
    '''
    def __init__(self):
        self.__search_service = SearchService()
        self.__search_validate = SearchValidate()
        self.__user_service = UserService()
        self.__user_validate = UserValidate()
        self.__schema = CourseSchema()
        self.__service = CourseService()

    def get(self):
        '''
        Función que obtiene todos los cursos

        return:
            - Lista de cursos en formato json
        '''
        return self.__schema.dump(self.__service.get_all(), many=True), 201
                
    def post(self):
        '''
        Función que guarda los curso en la base de datos

        return:
            - Mensaje de éxito o error 404
        '''
        json = request.json

        if not json:
            return "No json data", 400

        elif "courses" and "discord_id" in json:
            return self.post_course(courses_urls = request.json["courses"], discord_id = request.json["discord_id"])

        else:
            return "Incorrect json data", 400
            

    def post_course(self, courses_urls, discord_id):
        '''
        Función que guarda los curso en la base de datos

        args:
            - courses_urls: Lista de url de los cursos
            - discord_id: ID del usuario en discord
        return:
            - Mensaje de éxito o error 404
        '''

        @self.__user_validate.get_user(discord_id = discord_id)
        def validater():
            user_model = self.__user_service.get_by_discord_id(discord_id = discord_id)

            @self.__search_validate.get_by_user_id(user_id = user_model.id)
            def validater():
                search_model = self.__search_service.get_by_user_id(user_id = user_model.id)
                search_id = search_model.id

                for i in range(len(courses_urls)):
                    course = self.__service.get_by_course_url(course_url = courses_urls[i][1])

                    if course:
                        self.__service.add_count(id = course.id)
                        if (i == len(courses_urls) - 1):
                            return "All course models saved", 201
                        continue
                    
                    data = {
                        "url": courses_urls[i][1],
                        "title": courses_urls[i][0],
                        "search_id": search_id
                    }

                    model = self.__schema.load(data)
                    model = self.__service.add(model)
                    
                    if (i == len(courses_urls) - 1):
                        return "All course models saved", 201
                        
            return validater()
        return validater()        