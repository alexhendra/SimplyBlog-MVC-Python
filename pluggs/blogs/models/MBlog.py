from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from web_app.models import db


class Blog(db.Model):
    __tablename__ = 'blog'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    title = Column(String)
    content = Column(String)
    image_id = Column(String)
    image_loc = Column(String)
    thumbnail = Column(String)
    page_id = Column(Integer, ForeignKey('page.id'))
    page = relationship('Page', backref='Blog', cascade='all, delete')
    createdby = Column(String)
    createddate = Column(DateTime)
    modifiedby = Column(String)
    modifieddate = Column(DateTime)
