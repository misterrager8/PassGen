from flask_login import UserMixin
from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship

from PassGen import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(Text)
    password = Column(Text)
    accounts = relationship("Account", lazy="dynamic")

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)


class Account(db.Model):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    user_ = Column(Text)
    pass_ = Column(Text)
    hint = Column(Text)
    date_modified = Column(DateTime)
    color = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __init__(self, **kwargs):
        super(Account, self).__init__(**kwargs)
