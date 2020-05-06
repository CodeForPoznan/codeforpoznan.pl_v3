from marshmallow import Schema, fields, validate


class ParticipantSchema(Schema):
    class Meta:
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "github",
            "hacknights",
            "phone",
            "slack",
        )

        dump_only = ("id", "hacknights")

    first_name = fields.Str(required=True, validate=[validate.Length(min=3, max=50)])
    last_name = fields.Str(required=True, validate=[validate.Length(min=3, max=50)])
    email = fields.Email(required=True, validate=[validate.Length(min=3, max=200)])
    github = fields.Str(required=True, validate=[validate.Length(min=1, max=39)])
    hacknights = fields.Nested("HacknightSchema", exclude=("participants",), many=True)
    phone = fields.Str(validate=[validate.Length(max=13)])
    slack = fields.Str(validate=[validate.Length(max=21)])
