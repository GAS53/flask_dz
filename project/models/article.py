from datetime import datetime

from sqlalchemy import Column, String, DateTime, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from models.database import db
from models.tags import artickle_tag

class Article(db.Model):
    id = db.Column(Integer, primary_key=True)
    author_id = db.Column(Integer, ForeignKey("author.id"))
    author = relationship("Author", back_populates="articles")
    title = db.Column(String(200), nullable=False, default="", server_default="")
    body = db.Column(String(2000), nullable=False, default="", server_default="")
    dt_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    tags = relationship('Tag', 
                        secondary=artickle_tag,
                        back_populates='articles',)