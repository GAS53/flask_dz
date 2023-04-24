from flask import Blueprint, render_template, redirect, flash, url_for, request
from flask_login import logout_user, login_user
from werkzeug.security import check_password_hash

from models.user import User
from user.auth import auth, login_required

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


# @auth.route('/login')
# def login():
#     return render_template('/user/login.html')


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