from sqlalchemy import Column, Integer, String, Boolean
from flask_login import UserMixin

from models.database import db


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    login = Column(String(36), unique=True, nullable=False)
    email = Column(String(86), nullable=False, unique=True)
    pswd = Column(String(86), nullable=False)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return f'пользователь {self.login} id-{self.id}'