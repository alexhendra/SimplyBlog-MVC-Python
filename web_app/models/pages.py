from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from web_app.models import db
from web_app.models.sites import Site


class Page(db.Model):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String)
    site_id = Column(Integer, ForeignKey('site.id'))
    site = relationship('Site', backref='Page', cascade='all, delete')
    createdby = Column(String)
    createddate = Column(DateTime)
    modifiedby = Column(String)
    modifieddate = Column(DateTime)

    def insert(self):
        db.session.add(self)
        db.session.commit()
