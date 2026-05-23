from src.controller.task_controller import (
    create_task_controller,
    delete_task_controller,
    get_completed_by_range_controller, 
    get_all_task_controller, get_task_controller,
    update_task_controller)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.database import get_db
from src.models.schemas import CreateTask, TaskUpdate, TaskResponse, CompleteTaskResponse

router = APIRouter(prefix='/tasks', tags=["tasks"])

@router.get("/completed", response_model=CompleteTaskResponse)
def get_completed_by_range(range:str, db: Session = Depends(get_db)):
    return get_completed_by_range_controller(range, db)

@router.post("")
def create_task(task_data:CreateTask, db: Session = Depends(get_db)):
    return create_task_controller(task_data, db)

@router.delete("/{task_id}")
def delete_task(task_id:int, db: Session = Depends(get_db)):
    return delete_task_controller(task_id, db)

@router.get("")
def get_all_tasks(db: Session = Depends(get_db)):
    return get_all_task_controller(db)

@router.get("/{task_id}")
def get_task(task_id:int, db: Session = Depends(get_db)):
    return get_task_controller(task_id, db)

@router.put("/{task_id}")
def update_task(task_id:int, update_data:TaskUpdate, db: Session = Depends(get_db)):
    return update_task_controller(task_id,update_data, db)
