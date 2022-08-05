from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL: str = "postgresql://anastasiya:belhard@localhost:5432/bh57"
DATABASE_ASYNC_URL: str = "postgresql+asyncpg://anastasiya:belhard@localhost:5432/bh57"
engine = create_engine(DATABASE_URL)
async_engine = create_engine(DATABASE_ASYNC_URL_URL)
Session = sessionmaker(bind=engine)


def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper


def create_async_session(funk):
    async def wrapper(**kwargs):
        async with AsyncSession(bind=async_engine) as sesion:
            return await funk(**kwargs, sesion=sesion)
    return wrapper
