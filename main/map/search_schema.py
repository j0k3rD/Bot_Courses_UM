from marshmallow import Schema, fields, validate, post_load, post_dump
from main.models import SearchModel
from .user_schema import UserSchema


class SearchSchema(Schema):
    
    id = fields.Int(dump_only=True)
    keywords = fields.Str(required=True, validate=validate.Length(min=1))
    date = fields.DateTime(required=False)
    user_id = fields.Int(required=True, validate=validate.Range(min=0))
    user = fields.Nested(UserSchema)

    @post_load
    def make_search(self, data, **kwargs):
        return SearchModel(**data)

    SKIP_VALUES = ['user_id']
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items() if key not in self.SKIP_VALUES
        }