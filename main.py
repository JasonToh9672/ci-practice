from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

todos = {1: {"id": 1, "title": "Buy milk", "done": False}}   # fake "database": a dict, id → todo


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[todo_id]


@app.post("/todos")
def create_todo(todo: TodoCreate):
    new_id = max(todos) + 1                  # biggest id so far + 1
    todos[new_id] = {"id": new_id, "title": todo.title, "done": False}
    return todos[new_id]

# 5
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    else:
        del todos[todo_id] #use del or pop to delete from dictionary
        return {"deleted": todo_id}