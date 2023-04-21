from flask import Flask


from article.views import article
from user.views import user
from user.auth import auth, login_manager
from models.database import db
from config import ProductionConfig, DevelopmentConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(article)
    app.register_blueprint(user)
    app.register_blueprint(auth, url_prefix="/auth")
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    db.init_app(app)
    return app


    


