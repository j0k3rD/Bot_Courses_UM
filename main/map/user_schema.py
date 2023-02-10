from marshmallow import Schema, fields, validate, post_load
from main.models import UserModel


class UserSchema(Schema):
    '''
    Esquema de la entidad User para serializar y deserializar formato json.

    param:
        - Schema: Clase de la cual hereda    
    '''
    id = fields.Int(dump_only=True)
    discord_id = fields.Int(required=True, validate=validate.Range(min=0))
    name = fields.Str(required=True, validate=validate.Length(min=1))

    @post_load
    def make_user(self, data, **kwargs):
        '''
        Función que crea un objeto de tipo UserModel a partir de un diccionario

        args:
            - data: diccionario con los datos del curso
        return:
            - Objeto de tipo UserModel
        '''
        return UserModel(**data)