from flask_restful import Resource
from flask import request
from main.services import SearchService, UserService
from main.map import SearchSchema, UserSchema
from main.validate import SearchValidate, UserValidate

validate = SearchValidate()
schema = SearchSchema()
service = SearchService()


class Search(Resource):
    '''
    Clase que representa el controlador de la entidad Search

    param:
        - Resource: Clase de la cual hereda
    '''

    def get(self, id):
        '''
        Función que obtiene un busqueda por su id

        args:
            - id: id de la busqueda
        return:
            - Busqueda en formato json o error 404
        '''
        @validate.validate_search(id)
        def validater():
            return schema.dump(service.get_by_id(id)), 201
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

    def get(self):
        '''
        Función que obtiene todos las busquedas

        return:
            - Lista de busquedas en formato json
        '''
        
        model = schema.dump(service.get_all(), many=True)
        return model, 201

    def post(self):
        '''
        Función que guarda la busqueda

        return:
            - Busqueda en formato json
        '''
        user_validate = UserValidate()
        user_service = UserService()
        user_schema = UserSchema()

        # Json values
        user_json = request.json
        keywords = user_json["keywords"]
        discord_id = user_json["discord_id"]

        @user_validate.get_user(discord_id = discord_id)
        def validater():

            user = user_schema.dump(user_service.get_by_discord_id(discord_id = discord_id))
            data = {
                "keywords": keywords,
                "user_id": user["id"]
            }
            model = schema.load(data) 
            return schema.dump(service.add(model)), 201

        return validater()