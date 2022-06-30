from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import sessionmaker

from .settings import settings

id = Column(Integer, primary_key=True)
email = Column(String, unique=True)
username = Column(String, unique=True)
password_hash = Column(String)

SQLALCHEMY_DATABASE_URL = f"postgresql://{id}:{email}@{username}/{password_hash}"

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False},
)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)

def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()
