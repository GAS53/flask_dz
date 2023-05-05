from flask import Blueprint, render_template
from models.author import Author
from sqlalchemy.sql import select
from models.database import db


authors = Blueprint("authors", __name__)


@authors.route("/", endpoint="list")
def authors_list():
    stmt = select(Author)
    print(stmt)
    authors = db.session.execute(stmt).all()
    return render_template("author/list.html", authors=authors)