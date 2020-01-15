from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    class Meta:
        fields = ("username", "password")

    username = fields.Str(required=True, validate=[validate.Length(min=3)])
    password = fields.Str(required=True, validate=[validate.Length(min=1)])
