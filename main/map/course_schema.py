from marshmallow import Schema, fields, validate, post_load, post_dump
from main.models import CourseModel
from .search_schema import SearchSchema


class CourseSchema(Schema):
    '''
    Esquema de la entidad Course para serializar y deserializar formato json.

    param:
        - Schema: Clase de la cual hereda    
    '''
    id = fields.Int(dump_only=True)
    url = fields.Str(required=True, validate=validate.Length(min=1))
    title = fields.Str(required=True, validate=validate.Length(min=1))
    count = fields.Int(required=False)
    search_id = fields.Int(required=True, validate=validate.Range(min=0))
    search = fields.Nested(SearchSchema)

    @post_load
    def make_course(self, data, **kwargs):
        '''
        Función que crea un objeto de tipo CourseModel a partir de un diccionario

        args:
            - data: diccionario con los datos del curso
        return:
            - Objeto de tipo CourseModel
        '''
        return CourseModel(**data)

    SKIP_VALUES = ['search_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }