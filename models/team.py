from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from database.db import Base
from sqlalchemy.orm import relationship

class Team(Base):
    __tablename__ = 'teams'

    id = mapped_column(String, primary_key=True)
    name = mapped_column(String)
    data_access_token = mapped_column(String, unique=True)
    access_id = mapped_column(String, unique=True)
    variables = relationship('Variable', cascade='all, delete-orphan')