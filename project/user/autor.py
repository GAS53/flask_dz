from flask import Blueprint, render_template
from models.autor import Author


authors = Blueprint("authors_app", __name__)


@authors.route("/", endpoint="list")
def authors_list():
    authors = Author.query.all()
    return render_template("author/list.html", authors=authors)