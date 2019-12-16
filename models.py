from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

    interests = relationship('Interest', back_populates='_user')


class Interest(Base):
    __tablename__ = 'interests'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    _user = relationship('User', back_populates='interests')
