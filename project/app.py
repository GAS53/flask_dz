from flask import Flask
from security import flask_bcrypt
from flask_combo_jsonapi import Api

from user.autor import authors
from article.views import article
from user.views import user
from user.auth import auth, login_manager
from admin import admin
from models.database import db
from config import ProductionConfig, DevelopmentConfig
from api.tag import TagDetail, TagList, UserList, UserDetail



def registr_api(app: Flask):
    api = Api(app)
    api.route(UserList, "user_list", "/api/1.0/users/")
    api.route(UserDetail, "user_detail", "/api/1.0/users/<int:id>/")
    api.route(TagList, "author_list", "/api/1.0/tags/" )
    api.route(TagDetail, "author_detail", "/api/1.0/tags/<int:id>/")


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(article, name='article')
    app.register_blueprint(user, name='test')
    app.register_blueprint(auth, name='auth')
    app.register_blueprint(authors, name='authors')
    

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    flask_bcrypt.init_app(app)
    db.init_app(app)
    admin.init_app(app)
    registr_api(app)
    # app.route(TagList, "author_list", "/api/1.0/authors/" )
    # app.route(TagDetail, "author_detail", "/api/1.0/authors/<int:id>/")


    return app