"""Provides Postgres database session object."""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from appconfig import get_config
from sqlalchemy.ext.asyncio import create_async_engine


config = get_config()
connection_string = 'postgresql+asyncpg://%s:%s@%s:%s/%s' % (
    config.SQLALCHEMY_USERNAME, config.SQLALCHEMY_PASSWORD, config.SQLALCHEMY_HOST, config.SQLALCHEMY_PORT,
    config.SQLALCHEMY_DATABASE)

engine = create_async_engine(
    connection_string,
    echo=True,
    future=True,
)

SessionLocal = sessionmaker(autocommit=config.SQLALCHEMY_AUTOCOMMIT, autoflush=config.SQLALCHEMY_AUTOFLUSH, bind=engine)
Base = declarative_base()


def get_session():
    """Return SQLAlchemy session object."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
