from email.policy import default
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DATETIME, BOOLEAN, Date
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base


class TMilestones(Base):
    __tablename__ = "t_milestones"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('m_projects.id'))
    assign_user_ids = Column(String(255), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    progress = Column(Integer, default=0)
    color = Column(String(9), nullable=True)
    created_at = Column(DATETIME, default=datetime.now)
    updated_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DATETIME, nullable=True)