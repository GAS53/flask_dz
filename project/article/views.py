from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
from flask_login import current_user
from models.article import Article
from forms.article import CreateArticleForm

from models.database import db
from models.autor import Author

article = Blueprint('article',__name__, url_prefix='/article', static_folder='../static')


@article.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("article/list.html", articles=articles)


@article.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
    article = Article.query.filter_by(id=article_id).one_or_none()
    if article is None:
        raise NotFound
    return render_template("article/details.html", article=article)

@article.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), body=form.body.data)
        db.session.add(article)
        if current_user.author:
            # use existing author if present
            article.author = current_user.author
        else:
            # otherwise create author record
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("articles_app.details", article_id=article.id))
    return render_template("articles/create.html", form=form, error=error)