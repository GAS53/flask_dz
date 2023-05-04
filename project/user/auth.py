from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models.user import User

from forms.user import LoginForm

auth = Blueprint("auth", __name__)
login_manager = LoginManager()  # инициализируем объект для обработки авторизации;
login_manager.login_view = "auth.login"  #  указываем view для авторизации


@login_manager.user_loader
def load_user(id):
    return User.query.filter_by(id=id).one_or_none() 


@login_manager.unauthorized_handler
def unauthorized(): # указываем обработку неавторизированной попытки доступа к защищённым view
    return redirect(url_for("auth.login"))


def login():
    if current_user.is_authenticated:
        return redirect("index")
    
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).one_or_none()
        if user is None:
            return render_template("user/login.html", form=form, error="username doesn't exist")
        if not user.validate_password(form.password.data):
            return render_template("user/login.html", form=form, error="invalid username or password")
        login_user(user)
        return redirect(url_for("index"))
    return render_template("user/login.html", form=form)





__all__ = ["login_manager", "auth", ]

