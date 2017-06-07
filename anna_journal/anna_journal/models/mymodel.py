from sqlalchemy import (
    Column,
    Index,
    Integer,
    Unicode,
    DateTime
)

from .meta import Base


class Journals(Base):
    __tablename__ = 'journals'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(DateTime)

Index('id', Journals.id, unique=True, mysql_length=255)
