from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required
from models.user import User

auth = Blueprint("auth", __name__)
login_manager = LoginManager()  # инициализируем объект для обработки авторизации;
login_manager.login_view = "auth.login"  #  указываем view для авторизации


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).one_or_none() 


@login_manager.unauthorized_handler
def unauthorized(): # указываем обработку неавторизированной попытки доступа к защищённым view
    return redirect(url_for("auth.login"))


__all__ = ["login_manager", "auth", ]

