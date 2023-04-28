from sqlalchemy import Column, Integer, String, Boolean, LargeBinary
from flask_login import UserMixin

from models.database import db
from security import flask_bcrypt


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    login = Column(String(36), unique=True, nullable=False)
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    email = Column(String(86), nullable=False, unique=True,  default="")
    is_staff = Column(Boolean, nullable=False, default=False)
    password = Column(LargeBinary, nullable=True)
    


    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, value):
        self.password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password):
        return flask_bcrypt.check_password_hash(self.password, password)


    def __repr__(self):
        return f'пользователь {self.login} id-{self.id}'