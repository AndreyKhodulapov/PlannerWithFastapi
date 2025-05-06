from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/", tags=["Start page"])
async def root() -> HTMLResponse:
    return HTMLResponse(
        """
        <body><h1 style="font-size: 50px; text-align: center">
        Welcome to my task tracker!
        </h1>
        <a href=http://127.0.0.1:8000/tasks>Go to task list</a>
        </body>
        """
    )

