from marshmallow import fields, Schema, validate


class MessageSchema(Schema):
    class Meta:
        fields = ('name', 'email', 'phone', 'content')

    name = fields.Str(
        required=True,
        validate=[validate.Length(max=50)])
    email = fields.Email(
        required=True,
        error_messages={'required':
                        {'message': 'Valid email is required',
                         'code': 400}})
    phone = fields.Str(validate=[validate.Length(max=9)])
    content = fields.Str(
        required=True,
        validate=[validate.Length(min=10, max=2000)],
        error_messages={'required':
                        {'message': 'Content of message is required',
                         'code': 400}})


message_schema = MessageSchema()
