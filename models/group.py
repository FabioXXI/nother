from sqlalchemy import Column, String, ForeignKey
from database.db import Base
from sqlalchemy.orm import relationship

class Group(Base):
    __tablename__ = 'groups'

    id = Column(String, primary_key=True)
    name = Column(String, unique=True)
    team_id = Column(String, ForeignKey('teams.id'))
    variables = relationship('Variable')