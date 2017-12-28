from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from web_app.models import db

from web_app.models.users import User
from web_app.models.roles import Role


class Authorizt(db.Model):
    __tablename__ = 'authorizt'
    id = Column(Integer, primary_key=True, autoincrement='auto')

    # http: // docs.sqlalchemy.org / en / latest / orm / join_conditions.html
    user_id = Column(String, ForeignKey('user.email'))
    user = relationship('User', backref='Authorizt', cascade='all,delete')

    role_id = Column(Integer, ForeignKey('role.id', name='fk_role_id'))
    role = relationship('Role', backref='Authorizt', cascade='all,delete')

    createdby = Column(String)
    createddate = Column(DateTime)
    modifiedby = Column(String)
    modifieddate = Column(DateTime)


