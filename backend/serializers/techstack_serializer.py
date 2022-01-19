from marshmallow import Schema, fields, validate


class TechStackSchema(Schema):
    class Meta:
        fields = ("id", "technology", "label", "teams")

        dump_only = ("id", "teams")

    technology = fields.Str(required=True, validate=[validate.Length(min=3, max=50)])
    label = fields.Str()
    teams = fields.Nested("TeamSchema", exclude=("tech_stack", "members"), many=True)
