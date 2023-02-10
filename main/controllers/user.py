from flask_restful import Resource
from flask import request
from main.services import UserService
from main.map import UserSchema
from main.validate import UserValidate


validate = UserValidate()
schema = UserSchema()
service = UserService()


class User(Resource):
    '''
    Clase que representa el controlador de la entidad User

    param:
        - Resource: Clase de la cual hereda
    '''

    def get(self, id):
        '''
        Función que obtiene un usuario por su id

        args:
            - id: id del usuario
        return:
            - Usuario en formato json o error 404
        '''
        @validate.validate_user(id)
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


class Users(Resource):
    '''
    Clase que representa el controlador de la entidad Users

    param:
        - Resource: Clase de la cual hereda
    '''

    def get(self):
        '''
        Función que obtiene todos los usuarios

        return:
            - Lista de usuarios en formato json
        '''
        model = schema.dump(service.get_all(), many=True)
        return model, 201

    def post(self):
        '''
        Función que verifica si un usuario ya existe y lo crea en caso de no existir

        return:
            - Usuario en formato json o usuario ya registrado 201
        '''
        # Json values.
        user_json = request.json
        discord_id = user_json["discord_id"]
        username = user_json["name"]

        # Validate if user already exists.
        if service.get_by_discord_id(discord_id):
            return f'User already exists by discord_id, {discord_id}', 201
    
        # Create user.
        data = {
            "discord_id": discord_id,
            "name": username
        }
        model = schema.load(data)
        return schema.dump(service.add(model)), 201