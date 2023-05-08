from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def get_todo_list(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todo")
async def retrieve_todo_list() -> dict:
    return {"todo_list": todo_list}

@todo_router.get("/todo/{id}")
async def get_single_todo(id: int = Path(..., title="The ID of the todo to retrieve."))->dict:
    for todo in todo_list:
        if todo.id == id:
            return {"todo" : todo}
    return {"message": "Todo not found"}
