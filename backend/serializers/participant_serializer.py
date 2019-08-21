from marshmallow import Schema, fields, validate


class ParticipantSchema(Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'github', 'hacknights', 'phone')

        dump_only = ('id', 'hacknights')

    first_name = fields.Str(required=True, validate=[validate.Length(max=50)])
    last_name = fields.Str(validate=[validate.Length(max=50)])
    email = fields.Email(validate=[validate.Length(max=200)])
    github = fields.Str(validate=[validate.Length(max=200)])
    hacknights = fields.Nested(
        'HacknightSchema',
        exclude=('participants', ),
        many=True
    )
    phone = fields.Str(validate=[validate.Length(max=13)])
