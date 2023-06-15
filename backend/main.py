from fastapi import FastAPI

from todo import todo_router
from game import game_router

from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

import modules.Rock_Paper_Scissors as RPS

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router)
app.include_router(game_router)

app.mount("/assets", StaticFiles(directory="../frontend/dist/assets"))


@app.get("/")
def index():
    return FileResponse("../frontend/dist/index.html")


# @app.get("/rps/{inputs}")
# def rps(inputs):
# PRS.Game.play(inputs)
