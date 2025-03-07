from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
from enum import StrEnum
from sqlalchemy import Enum


class ProjectStatus(StrEnum):
    PROCESSING = 'processing'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    FAILED = 'failed'


class TaskStatus(StrEnum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    FAILED = 'failed'


class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    project_name = Column(String)
    location = Column(String)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.PROCESSING)
    created_at = Column(DateTime, default=datetime.utcnow)
    tasks = relationship('Task', back_populates='project', lazy='joined')


class Task(Base):
    __tablename__ = 'tasks'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    project_id = Column(Integer, ForeignKey('projects.id'))
    project = relationship('Project', back_populates='tasks')
