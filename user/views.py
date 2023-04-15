from flask import Blueprint, render_template

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