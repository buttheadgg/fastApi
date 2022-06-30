import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ =  'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    password_hash = Column(String)

class  infoFile(Base):
    __tablename__ = 'inbox'

    id = Column(Integer, primary_key=True)
    code_request = Column(String)
    name_saved_file = Column(String)
    registration_date = Column(DateTime(timezone=True),default=datetime.datetime.utcnow())

    def __init__(self, code_request, name_saved_file):
        self.code_request = code_request
        self.name_saved_file = name_saved_file
