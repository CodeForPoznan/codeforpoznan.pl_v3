from marshmallow import Schema, fields, validate


class LoginSchema(Schema):
    class Meta:
        fields = ("github_username", "password")

    github_username = fields.Str(required=True, validate=[validate.Length(min=3)])
    password = fields.Str(required=True, validate=[validate.Length(min=1)])

class LoginGithubSchema(Schema):
    class Meta:
        fields = ("github_username",)

    github_username = fields.Str()
