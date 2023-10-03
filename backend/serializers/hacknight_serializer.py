from marshmallow import Schema, fields, pre_load


class HacknightSchema(Schema):
    class Meta:
        fields = ("id", "date", "participants")
        dump_only = ("id",)

    date = fields.Date(required=True)

    participants = fields.Nested(
        "ParticipantSchema", exclude=("hacknights",), many=True
    )
    date = fields.Date()


class DateFilterSchema(Schema):
    start_date = fields.Date(data_key="startDate")
    end_date = fields.Date(data_key="endDate")

    @pre_load
    def remove_empty_value(self, data, many, **kwargs):
        """Remove field whenever value is empty string."""
        return {key: value for key, value in data.items() if value}
