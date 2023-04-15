from flask import Flask

from article.views import article
from user.views import user

def create_app():
    app = Flask(__name__)
    app.register_blueprint(article)
    app.register_blueprint(user)
    return app


    


