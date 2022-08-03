from typing import Optional

from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.orm import Session, relationship
from sqlalchemy.exc import IntegrityError

from models import create_session, Category, Article
from schemas import CategorySchema, CategotyInDBSchema


class CRUDCategory:

    @staticmethod
    @create_session
    def add(category: CategorySchema, session: Session = None) -> Optional[CategotyInDBSchema]:
        category = Category(**category.dict())
        session.add(category)
        try:
            session.commit()
        except IntegrityError:
            pass
        else:
            session.refresh(category)
            return CategotyInDBSchema(**category.__dict__)

    @staticmethod
    @create_session
    def get(category_id: int, session: Session = None) -> Optional[CategotyInDBSchema]:
        category = session.execute(
            select(Category)
            .where(Category.id ==category_id)
        )
        category = category.first()
        if category:
            return CategotyInDBSchema(**category[0].__dict__)

    @staticmethod
    @create_session
    def get_all(parent_id: int = None, session: Session = None) -> list[CategotyInDBSchema]:
        if parent_id:
            categories = session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = session.execute(
                select(Category)
                .order_by(Category.id)
            )
        return [CategotyInDBSchema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_session
    def delere(category_id: int, session: Session = None) -> None:
        session.execute(
            delete(Category)
            .where(Category.id == category_id)
        )
        session.commit()

    @staticmethod
    @create_session
    def update(
            category: CategotyInDBSchema,
            session: Session = None
    ) -> bool:
        session.execute(
            update(Category)
            .where(Category.id == category.id)
            .values(**category.dict())
        )
        try:
            session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_session
    def get_articles(category_id: int, session: Session = None)-> list[tuple[Category, Article]]:
        response = session.execute(
            select(Category, Article)
            .join(Article, Category_id == Article.category_id)
            .where(Category.id == category_id)
        )
        return response.all()







