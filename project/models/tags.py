from sqlalchemy import Column, Integer, ForeignKey, String, Table
from sqlalchemy.orm import relationship
from models.database import db

artickle_tag = Table(
    'artickle_tag',
    db.metadata,
    Column('article.id', Integer, ForeignKey('article.id'), nullable=False),
    Column('tag_id', Integer, ForeignKey('tag.id'), nullable=False),
)

class Tag(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(36), default='', server_default="")
    articles = relationship('Article',
                            secondary=artickle_tag,
                            back_populates='tags')

    def __str__(self):
        return self.name