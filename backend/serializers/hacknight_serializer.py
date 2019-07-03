from marshmallow import Schema, fields


class HacknightSchema(Schema):
    class Meta:
        fields = ('id', 'date', 'participants')
        dump_only = ('id',)

    participants = fields.Nested(
        'ParticipantSchema',
        only=('id', 'github'),
        many=True
    )


hacknight_schema = HacknightSchema()
hacknights_schema = HacknightSchema(many=True)
