from marshmallow import Schema, fields, validate


class ParticipantSchema(Schema):
    class Meta:
        fields = (
            'id', 'name', 'lastname', 'email', 'github', 'hacknights', 'phone'
        )
        dump_only = ('id', 'hacknights')

    name = fields.Str(required=True, validate=[validate.Length(max=50)])
    lastname = fields.Str(validate=[validate.Length(max=50)])
    email = fields.Email(validate=[validate.Length(max=200)])
    github = fields.Str(validate=[validate.Length(max=200)])
    hacknights = fields.Nested(
        'HacknightSchema',
        exclude=('participants', ),
        many=True
    )
    phone = fields.Str(validate=[validate.Length(max=13)])


class HacknightSchema(Schema):
    class Meta:
        fields = ('id', 'date', 'participants')
        dump_only = ('id',)

    participants = fields.Nested(
        ParticipantSchema,
        only=('id', 'github'),
        many=True
    )


participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)
hacknight_schema = HacknightSchema()
hacknights_schema = HacknightSchema(many=True)
