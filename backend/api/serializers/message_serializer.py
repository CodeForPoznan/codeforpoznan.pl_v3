from marshmallow import fields, Schema, validate


class MessageSchema(Schema):
    class Meta:
        fields = ('name', 'email', 'phone', 'content')

    name = fields.Str(required=True)
    email = fields.Email(
        required=True,
        error_messages={'required':
                        {'message': 'Valid email is required',
                         'code': 400}})
    phone = fields.Str()
    content = fields.Str(
        required=True,
        validate=[validate.Length(min=10)],
        error_messages={'required':
                        {'message': 'Content of message is required',
                         'code': 400}})


message_schema = MessageSchema()
