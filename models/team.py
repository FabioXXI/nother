from sqlalchemy import Column, String
from database.db import Base
from sqlalchemy.orm import relationship

class Team(Base):
    __tablename__ = 'teams'

    id = Column(String, primary_key=True)
    name = Column(String)
    variables = relationship('Variable', cascade='all, delete-orphan')