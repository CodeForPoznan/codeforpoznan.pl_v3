from marshmallow import Schema, fields, validate


class TeamSchema(Schema):
    class Meta:
        fields = ("id", "project_name", "description", "project_url", "members")

        dump_only = ("id", "members")

    project_name = fields.Str(required=True, validate=[validate.Length(min=3, max=50)])
    description = fields.Str()
    project_url = fields.Str(validate=[validate.Length(max=200)])
    members = fields.Nested("ParticipantSchema", exclude=("hacknights",), many=True)
