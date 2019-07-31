from marshmallow import Schema, fields, validate


class ParticipantSchema(Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'email', 'github', 'phone')

    first_name = fields.Str(required=True, validate=[validate.Length(max=50)])
    last_name = fields.Str(validate=[validate.Length(max=50)])
    email = fields.Email(validate=[validate.Length(max=200)])
    github = fields.Str(validate=[validate.Length(max=200)])
    phone = fields.Str(validate=[validate.Length(max=13)])


participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)
