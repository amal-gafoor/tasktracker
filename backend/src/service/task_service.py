from sqlalchemy.orm import Session
from src.models.schemas import CreateTask,TaskUpdate,TaskResponse
from src.models.task_model import Task
from fastapi import HTTPException
from datetime import datetime, timedelta
from sqlalchemy import and_

def create_task(db: Session, task_data: CreateTask) -> Task:
    new_task = Task(title=task_data.title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_task_by_id(db:Session,task_id:int) -> Task:
    task=db.query(Task).filter(Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    return task

def get_all_task(db:Session) -> list[Task]:
    return db.query(Task).order_by(Task.created_at.desc()).all()

def update_task(db:Session, task_id:int, update_data:TaskUpdate) -> Task:
    task=db.query(Task).filter(Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="task not found")
    
    if update_data.title is not None:
        task.title = update_data.title

    if update_data.completed is not None:
        task.completed = update_data.completed
        task.completed_at=datetime.utcnow() if update_data.completed else None

    db.commit()
    db.refresh(task)

    return task

def delete_task(db:Session, task_id:int):
    task=db.query(Task).filter(Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    db.delete(task)
    db.commit()
    return {"message":f"task {task_id} is deleted succesfully"}

def get_completed_by_range(db:Session,range:str):
    range_map={"1d":1,"7d":7,"30d":30}
    if range not in range_map:
        raise HTTPException(status_code=404, detail="invalid range")
    
    cutoff = datetime.utcnow() - timedelta(days=range_map[range])

    tasks = db.query(Task).filter(and_(
        Task.completed == True,
        Task.completed_at >= cutoff)).order_by(
            Task.completed_at.desc()).all()
    
    task_data=[ TaskResponse.from_orm(task) for task in tasks ]

    return {"range":range,
            'total':len(task_data),
            "tasks":task_data}

                                       
        




    