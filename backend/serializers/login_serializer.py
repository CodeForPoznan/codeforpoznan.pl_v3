from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    class Meta:
        fields = ("github", "password")

    github = fields.Str(required=True, validate=[validate.Length(min=3)])
    password = fields.Str(required=True, validate=[validate.Length(min=1)])
