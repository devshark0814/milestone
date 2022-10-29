from email.policy import default
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DATETIME, BOOLEAN
from datetime import datetime
from sqlalchemy.orm import relationship

from database import Base


class TMilestones(Base):
    __tablename__ = "t_milestones"

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('m_projects.id'))
    assign_user_id = Column(Integer, ForeignKey('m_users.id'))
    progre_flag = Column(BOOLEAN, default=False)
    assign_start_date = Column(DATETIME, nullable=True)
    assign_end_date = Column(DATETIME, nullable=True)
    created_at = Column(DATETIME, default=datetime.now)
    updated_at = Column(DATETIME, default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DATETIME, nullable=True)