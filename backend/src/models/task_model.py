from pydantic import BaseModel, Field
from typing import Optional
class CreateTask(BaseModel):
    title: str = Field(...,min_length=1,max_length=30)


class TaskUpdate(BaseModel):
    title: Optional[str]
    completed: Optional[bool] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: str
    completed_at: Optional[str]

    class Config:
        from_attribute = True

class CompleteTaskResponse(BaseModel):
   range:str
   total:int
   tasks: list[TaskResponse]