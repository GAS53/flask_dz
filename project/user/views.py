from flask import Blueprint, current_app, render_template, redirect, flash, url_for, request
from flask_login import logout_user, login_user, current_user
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError

from models.user import User
from user.auth import auth, login_required
from forms.user import RegistrationForm
from models.database import db

user = Blueprint('user',__name__, url_prefix='/user', static_folder='../static')

USERS = [
    {'title': 'title first user',
    'body': 'body text for one user'},
    {'title': 'title Second user',
    'body': 'body text for Second user'}
]


@user.route('/')
def user_list():
    return render_template('/user/list.html', users=USERS)

@user.route('/<int:pk>')
def user_one(pk: int):
    try:
        user = USERS[pk]
    except IndexError:
        return render_template('not_found.html'), 404
    return render_template('/user/one.html', user=user)

@auth.route("/logout/", endpoint="logout")
@login_required
def logout(): # Также добавляем view для выхода. 
    logout_user()
    return render_template("index.html")

@auth.route("/secret/")
@login_required
def secret_view(): # вход под логином
    return "Super secret data"


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("user/login.html" )


    login = request.form.get("login")
    password = request.form.get("password")
    print(login, password)
    user = User.query.filter_by(login=login).first()

    if not user or not check_password_hash(user.pswd, password):
        flash("Check your login details")
        return redirect(url_for("auth.login"))
    login_user(user)
    return render_template("index.html")


@auth.route("/register", methods=["GET", "POST"], endpoint="register")
def register():
    if current_user.is_authenticated:
        return redirect("index")
    
    error = None
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).count():
            form.username.errors.append("Такое имя пользователя уже используется")
            return render_template("user/register.html", form=form)
    
    if User.query.filter_by(email=form.email.data).count():
        form.email.errors.append("Пользователь с таким email уже существует")
        return render_template("user/register.html", form=form)
    
    user = User(
        first_name=form.first_name.data,
        last_name=form.last_name.data,
        login=form.username.data,
        email=form.email.data,
        is_staff=False,)
    print(form.password.data)
    user.password = form.password.data
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        current_app.logger.exception("пользователь не создан")
        error = "пользователь не создан"
    else:
        current_app.logger.info(f"пользователь создан {user}")
        login_user(user)
        return redirect(url_for("index"))
    return render_template("user/register.html", form=form, error=error)
