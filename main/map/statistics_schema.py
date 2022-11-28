from marshmallow import Schema, fields, validate, post_load
from main.models import StatisticsModel


class StatisticsSchema(Schema):
    id = fields.Int(dump_only=True)
    user = fields.Int(required=True, validate=validate.Range(min=0))
    course = fields.Int(required=True, validate=validate.Range(min=0))
    
    @post_load
    def make_statistics(self, data, **kwargs):
        return StatisticsModel(**data)