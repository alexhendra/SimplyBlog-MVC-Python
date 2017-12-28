from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from web_app.models import db

from web_app.models.pages import Page


class Pluggine(db.Model):
    __tablename__ = 'pluggine'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String)
    position = Column(String)
    tablename = Column(String)
    viewname = Column(String)
    page_id = Column(Integer, ForeignKey('page.id'))
    page = relationship('Page', backref='Pluggine', cascade='all,delete')
    createdby = Column(String)
    createddate = Column(DateTime)
    modifiedby = Column(String)
    modifieddate = Column(DateTime)
