from marshmallow_jsonapi import Schema, fields

class AuthorSchema(Schema):
    class Meta:
        type_ = 'author'
        self_view = 'author_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'author_list'

    id = fields.Integer(as_string=True)
    # user = fields.String(allow_none=False, required=True)