from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    first_name = StringField("Имя")
    last_name = StringField("Фамилия")
    username = StringField("логин",[validators.DataRequired()],)
    email = StringField("Email", [
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, max=200),],
    filters=[lambda data: data and data.lower()],)
    
class RegistrationForm(UserBaseForm):
    password = PasswordField("новый пароль", [
        validators.DataRequired(),
        validators.EqualTo("confirm", message="Веденые пароли должны быть одинаковыми"),
        ], )
    confirm = PasswordField("Повторите пароль")
    submit = SubmitField("Регистрация")