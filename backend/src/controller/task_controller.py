from src.config.database import get_db
from src.models.schemas import CreateTask, TaskUpdate
from sqlalchemy.orm import Session
from fastapi import Depends
from src.service.task_service import create_task, delete_task, get_completed_by_range,get_task_by_id,get_all_task, update_task

def create_task_controller(
        task: CreateTask,
        db: Session = Depends(get_db)):
    return create_task(db,task)

def get_task_controller(
        task_id:int,
        db:Session = Depends(get_db)
):
    return get_task_by_id(db,task_id)

def get_all_task_controller(
        db:Session = Depends(get_db)
):
    return get_all_task(db)

def update_task_controller(
        task_id:int,
        update_data:TaskUpdate,
        db:Session = Depends(get_db)
):
    return update_task(db,task_id,update_data)

def delete_task_controller(
        task_id:int,
        db:Session = Depends(get_db)
):
    return delete_task(db,task_id)

def get_completed_by_range_controller(
        range:str,
        db:Session = Depends(get_db)
):
    return get_completed_by_range(db,range)
