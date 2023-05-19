from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
from flask_login import current_user

from sqlalchemy.orm import joinedload
from models.article import Article
from forms.article import CreateArticleForm
from models.database import db
from models.author import Author
from models.tags import Tag

article = Blueprint('article',__name__, url_prefix='/article', static_folder='../static')


@article.route("/", endpoint="list")
def articles_list():
    articles = Article.query.all()
    return render_template("article/list.html", articles=articles)


@article.route("/<int:article_id>/", endpoint="details")
def article_detals(article_id):
    article = Article.query.filter_by(id=article_id).options(joinedload(Article.tags)).one_or_none()
    if article is None:
        raise NotFound
    return render_template("article/details.html", article=article)

@article.route("/create/", methods=["GET", "POST"], endpoint="create")
@login_required
def create_article():
    error = None
    form = CreateArticleForm(request.form)

    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]

    if request.method == "POST" and form.validate_on_submit():
        article = Article(title=form.title.data.strip(), body=form.body.data)
        if form.tags.data: # если в форму были переданы теги (были выбраны)
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                article.tags.append(tag)
        
        db.session.add(article)
        if current_user.author:
            article.author = current_user.author
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            article.author = current_user.author
        try:
            db.session.commit()
        except IntegrityError:
            error = "Статья не была создана"
            current_app.logger.exception(error)
        else:
            return redirect(url_for("article.details", article_id=article.id))
    return render_template("article/create.html", form=form, error=error)