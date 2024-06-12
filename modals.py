from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Word(Base):
    _tablename_ = 'words'

    id = Column(Integer, primary_key=True)
    word = Column(String(5), nullable=False)
