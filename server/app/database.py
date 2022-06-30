from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .tables import infoFile
from .settings import settings
from fastapi import Depends

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

session = Session()

def create():
    infoFile.Base.metadata.create_all(infoFile.engine)


def add_new_data_to_database(code_request, name_saved_file):
    new_data = infoFile(code_request=code_request, name_saved_file=name_saved_file)
    session.add(new_data)


def search_data_by_code_request(code):
    return session.query(infoFile).filter_by(code_request=code).all()


def delete_data_by_code_request(code):
    session.query(infoFile).filter_by(code_request=code).delete()
    session.commit()