from sqlalchemy import Column, String, Integer, DateTime

from web_app.models import db


class Site(db.Model):
    __tablename__ = 'site'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String)
    createdby = Column(String)
    createddate = Column(DateTime)
    modifiedby = Column(String)
    modifieddate = Column(DateTime)

    def insert(self):
        db.session.add(self)
        db.session.commit()

