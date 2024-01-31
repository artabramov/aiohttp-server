"""Provides Postgres database session object."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import get_config
from sqlalchemy.ext.asyncio import create_async_engine
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession


config = get_config()
connection_string = 'postgresql+asyncpg://%s:%s@%s:%s/%s' % (
    config.PG_USERNAME, config.PG_PASSWORD, config.PG_HOST, config.PG_PORT,
    config.PG_DATABASE)

engine = create_async_engine(
    connection_string,
    echo=True,
    future=True,
)

Base = declarative_base()

def async_session_generator():
    return sessionmaker(
        autocommit=config.PG_AUTOCOMMIT, autoflush=config.PG_AUTOFLUSH, bind=engine, class_=AsyncSession
    )

@asynccontextmanager
async def get_session():
    try:
        async_session = async_session_generator()
        async with async_session() as session:
            yield session

    except:
        await session.rollback()
        raise

    finally:
        await session.close()
