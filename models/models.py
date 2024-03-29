from datetime import datetime

from sqlalchemy import Column, SmallInteger, VARCHAR, TIMESTAMP, Boolean, Integer, ForeignKey, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(24), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    is_blocked = Column(Boolean, default=False)


class Category(Base):
    __tablename__: str = "categories"

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(24), nullable=False)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"))


class Article(Base):
    __tablename__: str = "articles"

    id = Column(Integer, primary_key=True)
    category_id = Column(
        SmallInteger,
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False
    )
    title = Column(VARCHAR(50), nullable=False)
    body = Column(VARCHAR(1024), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)


class ArticleCommert(Base):
    __tablename__: str = "article_comments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"), nullable=False)
    comment = Column(VARCHAR(140), nullable=False)
    data_create = Column(TIMESTAMP, default=datetime.utcnow())


