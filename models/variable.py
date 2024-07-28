from sqlalchemy.orm import mapped_column
from sqlalchemy import String, ForeignKey
from database.db import Base

class Variable(Base):
    __tablename__ = 'variables'

    id = mapped_column(String, primary_key=True)
    name = mapped_column(String, unique=True)
    type = mapped_column(String)
    value = mapped_column(String)
    team_id = mapped_column(String, ForeignKey('teams.id'))