from marshmallow import Schema, fields, validate


class ParticipantSchema(Schema):
    class Meta:
        fields = ('name', 'lastname', 'email', 'github', 'phone')

    name = fields.Str(required=True, validate=[validate.Length(max=50)])
    lastname = fields.Str(validate=[validate.Length(max=50)])
    email = fields.Email(validate=[validate.Length(max=200)])
    github = fields.Str(validate=[validate.Length(max=200)])
    phone = fields.Str(validate=[validate.Length(max=13)])


participant_schema = ParticipantSchema()
participants_schema = ParticipantSchema(many=True)
