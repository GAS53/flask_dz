from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, TextAreaField, SubmitField, validators


class CreateArticleForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()],)
    body = TextAreaField("Body", [validators.DataRequired()],)
    tags = SelectMultipleField("Tags", coerce=int)
    submit = SubmitField("Publish")