from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from web_app.models import db


class Role(db.Model):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True, autoincrement='auto')
    name = Column(String)
    user_id = Column(String, ForeignKey('user.email'))
    user = relationship('User', backref='Role', cascade='all,delete')
    createdby = Column(String)
    createddate = Column(DateTime)
    modifiedby = Column(String)
    modifieddate = Column(DateTime)
