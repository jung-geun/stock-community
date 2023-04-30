from fastapi import FastAPI
from todo import todo_router
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/hello")
async def hello() -> dict:
    return {"message": "Hello World"}


@app.get("/svelte")
async def hello_svelte() -> dict:
    return {"message": "Hello svelte"}

app.include_router(todo_router)
app.mount("/assets", StaticFiles(directory="frontend/dist/assets"))
@app.get("/")
def index():
    return FileResponse("frontend/dist/index.html")