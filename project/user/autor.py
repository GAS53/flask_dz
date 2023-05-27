from flask import Blueprint, render_template
from models.author import Author
from sqlalchemy.sql import select
from models.database import db
from flask_apispec import marshal_with
from schemas.Autors import AuthorSchema

from models.article import Article

authors = Blueprint("authors", __name__)

@marshal_with(AuthorSchema(many=True))
@authors.route("/", endpoint="list")
def authors_list():
    authors = Author.query.all()
    return render_template("author/list.html", authors=authors)


class AuthorDetailEvents(EventsResource):
    def event_get_articles_count(self, **kwargs):
        return {"count": Article.query.filter(Article.author_id == kwargs["id"]).count()}
