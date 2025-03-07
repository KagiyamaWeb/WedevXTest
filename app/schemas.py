from pydantic import BaseModel
from datetime import datetime
from typing import List

class TaskBase(BaseModel):
    name: str
    status: str

class ProjectCreate(BaseModel):
    project_name: str
    location: str

class ProjectResponse(ProjectCreate):
    id: int
    status: str
    created_at: datetime
    tasks: List[TaskBase]

    class Config:
        orm_mode = True
