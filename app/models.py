from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String)
    location = Column(String)
    status = Column(String, default='processing')
    created_at = Column(DateTime, default=datetime.utcnow)
    tasks = relationship('Task', back_populates='project')

class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String, default='pending')
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('Project', back_populates='tasks')
