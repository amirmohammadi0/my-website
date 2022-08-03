from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey, Text
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    is_active = Column(Boolean,default=True)
    items = relationship("Article", back_populates="user")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    content = Column(Text, index=True)
    published = Column(Boolean)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="items")