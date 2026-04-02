from sqlalchemy import Table
from sqlalchemy.orm import DeclarativeBase
import settings  # noqa
from bot.db import engine


class Base(DeclarativeBase):
    pass
 

class User(Base):
    __table__ = Table("user", Base.metadata, autoload_with=engine)

    def __repr__(self):
        values = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return f"User({values})"


class Message(Base):
    __table__ = Table("message", Base.metadata, autoload_with=engine)

    def __repr__(self):
        values = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return f"User({values})"


class Chat(Base):
    __table__ = Table("chat", Base.metadata, autoload_with=engine)

    def __repr__(self):
        values = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return f"User({values})"


class ChatUser(Base):
    __table__ = Table("chat_user", Base.metadata, autoload_with=engine)

    def __repr__(self):
        values = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return f"User({values})"
