from sqlalchemy import Column, String, ForeignKey
from database.db import Base

class Variable(Base):
    __tablename__ = 'variables'

    id = Column(String, primary_key=True)
    name = Column(String, unique=True)
    type = Column(String)
    value = Column(String)
    point_to = Column(String, ForeignKey('variables.id'), nullable=True)
    group = Column(String, ForeignKey('groups.id'), nullable=True)
    team_id = Column(String, ForeignKey('teams.id'))