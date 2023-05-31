from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField


class UserBaseForm(FlaskForm):
    login = StringField("логин",[validators.DataRequired()],)
    first_name = StringField("Имя")
    last_name = StringField("Фамилия")
    
    email = StringField("Email", [
        validators.DataRequired(),
        validators.Email(),
        validators.Length(min=6, max=200),],
    filters=[lambda data: data and data.lower()],)
    
class RegistrationForm(UserBaseForm):
    password = PasswordField("Введите пароль", [
        validators.DataRequired(),
        validators.EqualTo("confirm", message="Веденые пароли должны быть одинаковыми"),
        ], )
    confirm = PasswordField("Повторите пароль")
    submit = SubmitField("Регистрация")


class LoginForm(FlaskForm):
    login = StringField("login", [validators.DataRequired()],)
    password = PasswordField("Password", [validators.DataRequired()],)
    submit = SubmitField("Login")