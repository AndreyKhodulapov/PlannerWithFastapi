from typing import Annotated
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Turn on the database")
    await create_tables()
    yield
    print("Turn off the database")
    await delete_tables()


app = FastAPI(lifespan= lifespan)


class STaskAdd(BaseModel):
    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}


@app.get("/tasks")
def get_all_tasks():
    return {"data": tasks}