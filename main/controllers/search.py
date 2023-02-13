from flask_restful import Resource
from flask import request
from main.services import SearchService, UserService
from main.map import SearchSchema, UserSchema
from main.validate import SearchValidate, UserValidate

class Search(Resource):
    '''
    Clase que representa el controlador de la entidad Search

    param:
        - Resource: Clase de la cual hereda
    '''

    def __init__(self):
        self.__validate = SearchValidate()
        self.__schema = SearchSchema()
        self.__service = SearchService()


    def get(self, id):
        '''
        Función que obtiene un busqueda por su id

        args:
            - id: id de la busqueda
        return:
            - Busqueda en formato json o error 404
        '''
        @self.__validate.validate_search(id)
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


class Searchs(Resource):
    '''
    Clase que representa el controlador de la entidad Searchs

    param:
        - Resource: Clase de la cual hereda
    '''
    def __init__(self):
        self.__user_validate = UserValidate()
        self.__schema = SearchSchema()
        self.__user_service = UserService()
        self.__user_schema = UserSchema()
        self.__service = SearchService()

    def get(self):
        '''
        Función que obtiene todos las busquedas

        return:
            - Lista de busquedas en formato json
        '''
        
        model = self.__schema.dump(self.__service.get_all(), many=True)
        return model, 201

    def post(self):
        '''
        Función que guarda la busqueda

        return:
            - Busqueda en formato json
        '''
        

        # Json values
        user_json = request.json
        keywords = user_json["keywords"]
        discord_id = user_json["discord_id"]

        @self.__user_validate.get_user(discord_id = discord_id)
        def validater():

            user = self.__user_schema.dump(self.__user_service.get_by_discord_id(discord_id = discord_id))
            data = {
                "keywords": keywords,
                "user_id": user["id"]
            }
            model = self.__schema.load(data) 
            return self.__schema.dump(self.__service.add(model)), 201

        return validater()