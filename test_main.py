from fastapi.testclient import TestClient    # a "pretend browser" that sends requests to your app

from main import app                        # import the app object itself

client = TestClient(app)                     # create it once, for all the tests in this file

def test_get_existing_todo():
    response = client.get("/todos/1")                       # like typing the URL in a browser
    assert response.status_code == 200                     # check the status code
    assert response.json() == {"id": 1, "title": "Buy milk", "done": False}   # check the body

def test_get_missing_todo_returns_404():
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}

def test_create_todo():
    response = client.post("/todos", json={"title": "Study pytest"})   # send JSON, like a POST from /docs
    assert response.status_code == 200
    assert response.json()["title"] == "Study pytest"
    assert response.json()["done"] is False                 # "is False", same idea as "is None"

def test_create_todo_empty_title_returns_422():
    response = client.post("/todos", json={"title": ""})    # breaks min_length=1
    assert response.status_code == 422                      # FastAPI/Pydantic rejects it automatically


def test_create_todo_long_title():
    response = client.post("/todos", json = {"title": "a" * 101})
    assert response.status_code == 422


def test_delete_todo_missing_id():
    response = client.delete("/todos/999")
    assert response.status_code == 404



def test_delete_works():
    response = client.post("/todos", json={"title": "What is RAG"})
    todo_id = response.json()["id"]
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == {'deleted': todo_id}
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}
