from marshmallow import Schema, fields, validate, post_load
from main.models import UserModel


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    discord_id = fields.Int(required=True, validate=validate.Range(min=0))
    name = fields.Str(required=True, validate=validate.Length(min=1))
    deleted = fields.Boolean(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return UserModel(**data)