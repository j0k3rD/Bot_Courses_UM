from marshmallow import Schema, fields, validate, post_load
from main.models import StatisticModel
from .user_schema import UserSchema
from .course_schema import CourseSchema


class StatisticsSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True, validate=validate.Range(min=0))
    user = fields.Nested(UserSchema)
    course_id = fields.Int(required=True, validate=validate.Range(min=0))
    course = fields.Nested(CourseSchema)
    
    @post_load
    def make_statistics(self, data, **kwargs):
        return StatisticModel(**data)