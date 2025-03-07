from typing import List

from pydantic import BaseModel, constr, validator
from datetime import datetime
from app.models import Project, Task, ProjectStatus, TaskStatus


class TaskBase(BaseModel):
    name: str
    status: TaskStatus

    class Config:
        orm_mode = True
        use_enum_values = True  # Serialize enums to strings


class ProjectCreate(BaseModel):
    project_name: str
    location: str


class ProjectResponse(ProjectCreate):
    id: int
    status: ProjectStatus
    created_at: datetime
    tasks: List[TaskBase]
    
    class Config:
        orm_mode = True
        use_enum_values = True  # Serialize enums to strings