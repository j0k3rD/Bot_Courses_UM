from marshmallow import Schema, fields, validate, post_load
from main.models import SearchModel


class SearchSchema(Schema):
    id = fields.Int(dump_only=True)
    keyword = fields.Str(required=True, validate=validate.Length(min=1))
    date = fields.DateTime(required=True)
    user_id = fields.Int(required=True, validate=validate.Range(min=0))

    @post_load
    def make_search(self, data, **kwargs):
        return SearchModel(**data)