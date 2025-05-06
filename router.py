from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

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
async def get_all_tasks() -> dict[str, list[STask]]:
    tasks = await TaskRepository.find_all()
    return {"tasks": tasks}


