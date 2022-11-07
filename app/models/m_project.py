from email.policy import default
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DATETIME, Date
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base


class MProject(Base):
    __tablename__ = "m_projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    description = Column(Text, nullable=True)
    priority = Column(Integer, nullable=True)
    sale_cost = Column(Integer, nullable=True)
    planned_release_date = Column(Date, nullable=True)
    fact_release_date = Column(Date, nullable=True)
    created_at = Column(DATETIME, default=datetime.now)
    updated_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DATETIME, nullable=True)