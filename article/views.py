from flask import Blueprint, render_template
from flask_login import login_required

article = Blueprint('article',__name__, url_prefix='/article', static_folder='../static')

ARTICLES = [
    {'title': 'title 1',
     'body': 'body 1'},
     {'title': 'title 2',
     'body': 'body 2'},
    ]

@article.route('/')
def article_list():
    return render_template('/article/list.html', articles=ARTICLES)

@article.route('/<int:pk>')
@login_required
def article_one(pk: int):
    try:
        article = ARTICLES[pk]
    except IndexError:
        return render_template('not_found.html'), 404
    return render_template('/article/one.html', article=article)