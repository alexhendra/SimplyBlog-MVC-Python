from sqlalchemy import Column, String, DateTime
from web_app.models import db


class User(db.Model):
    __tablename__ = 'user'
    email = Column(String, primary_key=True)
    userid = Column(String)
    name = Column(String)
    createdby = Column(String)
    createddate = Column(DateTime)
    modifiedby = Column(String)
    modifieddate = Column(DateTime)

    def insert(self):
        db.session.add(self)
        db.session.commit()
