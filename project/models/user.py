from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from flask_login import UserMixin

from security import flask_bcrypt

from models.database import db
import config

class User(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    login = db.Column(String(36), unique=True, nullable=False)
    first_name = db.Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = db.Column(String(120), unique=False, nullable=False, default="", server_default="")
    email = db.Column(String(86), nullable=False, unique=True,  default="")
    is_staff = db.Column(Boolean, nullable=False, default=False)
    pswd = db.Column(String(128), nullable=True)
    author = relationship("Author", uselist=False, back_populates="user")


    @property
    def password(self):
        print(f'passord getter')
        return self.password
    

    @password.setter
    def password(self, value):
        print(f'passord setter {value}')
        self.pswd = flask_bcrypt.generate_password_hash(value) # , config.Config.SECRET_KEY 

    def validate_password(self, password):
        return flask_bcrypt.check_password_hash(self.pswd, password)


    def __repr__(self):
        return f'пользователь {self.login} id-{self.id}'