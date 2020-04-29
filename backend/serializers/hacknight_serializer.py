from marshmallow import Schema, fields


class HacknightSchema(Schema):
    class Meta:
        fields = ("id", "date", "participants")
        dump_only = ("id",)

    date = fields.Date(required=True)

    participants = fields.Nested(
        "ParticipantSchema", exclude=("hacknights",), many=True
    )
    date = fields.Date()
