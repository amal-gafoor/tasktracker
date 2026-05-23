from src.controller.task_controller import (
    create_task_controller,
    delete_task_controller,
    get_completed_by_range_controller, 
    get_all_task_controller, get_task_controller,
    update_task_controller)
from fastapi import APIRouter, Depends
from src.models.schemas import CreateTask, TaskUpdate, TaskResponse, CompleteTaskResponse

router = APIRouter(prefix='/tasks', tags=["tasks"])

@router.get("/completed", response_model=CompleteTaskResponse)
def get_completed_by_range(range:str):
    return get_completed_by_range_controller(range)

@router.post("")
def create_task(task_data:CreateTask):
    return create_task_controller(task_data)

@router.delete("{task_id}")
def delete_task(task_id:int):
    return delete_task_controller(task_id)

@router.get("")
def get_all_tasks():
    return get_all_task_controller

@router.get("/{task_id}")
def get_task(task_id=int):
    return get_task_controller(task_id)

@router.put("{task_id}")
def update_task(task_id:int, update_data:TaskUpdate):
    return update_task_controller(task_id,update_data)
