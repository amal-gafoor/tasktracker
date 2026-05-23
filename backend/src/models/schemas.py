from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional
class CreateTask(BaseModel):
    title: str = Field(...,min_length=1,max_length=30)


class TaskUpdate(BaseModel):
    title: Optional[str]
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    completed: bool
    created_at: datetime
    completed_at: Optional[datetime]

class CompleteTaskResponse(BaseModel):
   range:str
   total:int
   tasks: list[TaskResponse]



