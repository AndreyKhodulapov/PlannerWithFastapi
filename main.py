from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Turn on the database")
    await create_tables()
    yield
    print("Turn off the database")
    await delete_tables()


app = FastAPI(lifespan= lifespan)
app.include_router(tasks_router)

