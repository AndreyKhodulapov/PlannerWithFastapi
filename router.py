from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId
from sqlalchemy.exc import NoResultFound

router = APIRouter(
    prefix="/tasks",
    tags=["TASKS"]
)

@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return STaskId(task_id=task_id)


@router.get("")
async def get_all_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks

@router.get("/{task_id}")
async def get_one_task(task_id: int) -> STask:
    try:
        task = await TaskRepository.find_one_by_id(task_id)
        return task
    except NoResultFound:
        raise HTTPException(status_code=404, detail=f"There is no task with {task_id=}")




