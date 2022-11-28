from marshmallow import Schema, fields, validate, post_load
from main.models import CourseModel


class CourseSchema(Schema):
    
    id = fields.Int(dump_only=True)
    url = fields.Str(required=True, validate=validate.Length(min=1))
    title = fields.Str(required=True, validate=validate.Length(min=1))
    count = fields.Int(required=True, validate=validate.Range(min=0))

    @post_load
    def make_course(self, data, **kwargs):
        return CourseModel(**data)