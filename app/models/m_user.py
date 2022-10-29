from email.policy import default
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DATETIME
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "m_users"

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    image = Column(String(255), nullable=True)
    created_at = Column(DATETIME, default=datetime.now)
    updated_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DATETIME, nullable=True)