from marshmallow import Schema, fields, validate, post_load, post_dump
from main.models import SearchModel
from .user_schema import UserSchema


class SearchSchema(Schema):
    '''
    Esquema de la entidad Search para serializar y deserializar formato json.

    param:
        - Schema: Clase de la cual hereda    
    '''
    id = fields.Int(dump_only=True)
    keywords = fields.Str(required=True, validate=validate.Length(min=1))
    date = fields.DateTime(required=False)
    user_id = fields.Int(required=True, validate=validate.Range(min=0))
    user = fields.Nested(UserSchema)

    @post_load
    def make_search(self, data, **kwargs):
        '''
        Función que crea un objeto de tipo SearchModel a partir de un diccionario

        args:
            - data: diccionario con los datos del curso
        return:
            - Objeto de tipo SearchModel
        '''
        return SearchModel(**data)

    SKIP_VALUES = ['user_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }