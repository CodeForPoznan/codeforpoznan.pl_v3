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
    email = fields.Email(required=True, validate=[validate.Email()])
    github = fields.Str(
        required=True,
        validate=[
            validate.Length(max=38),
            validate.Regexp("^[a-zA-Z0-9][a-zA-Z0-9._-]*$"),
        ],
    )
    hacknights = fields.Nested("HacknightSchema", exclude=("participants",), many=True)
    phone = fields.Str(
        validate=[
            validate.Length(max=13),
            validate.Regexp("^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$"),
        ],
        allow_none=True,
    )
    slack = fields.Str(
        validate=[
            validate.Length(max=21),
            validate.Regexp("^[a-zA-Z0-9][a-zA-Z0-9._-]*$"),
        ],
        allow_none=True,
    )
