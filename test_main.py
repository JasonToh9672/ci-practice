# cd Exercise before running python -m pytest, because we have same test file name inside Exercise folder and 17_testing folder
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

# 4
def test_create_todo_long_title():
    response = client.post("/todos", json = {"title": "a" * 101})
    assert response.status_code == 422

# 6(a)
def test_delete_todo_missing_id():
    response = client.delete("/todos/999")
    assert response.status_code == 404


# 6(b)
def test_delete_works():
    response = client.post("/todos", json={"title": "What is RAG"})
    todo_id = response.json()["id"]
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == {'deleted': todo_id}
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}

# 6(c)
# we should not let one test affect another test
# if you delete todos 1, other test with the todo_id 1 will fail
# creating your own todo then delete your own todo is better

# 7
# with small test, each with specific name and function, we can know which part is going wrong from the name itself, then adjust the function





"""
What happens:

- TestClient(app) is a pretend browser. It sends requests directly to your app object, so there’s no server and no port. That’s why it’s fast.
- client.get(...), client.post(..., json={...}): the method matches the HTTP method. There are also client.put(...) and client.delete(...).
- The response is just like the one from requests in Session 10: .status_code and .json(). You already know this.
- What to check in API tests: the status code (200, 404, 422) and the body. These are exactly the things in your README’s endpoint table.

⚠️ One thing to watch: test_create_todo adds a todo to the todos dict, and that change stays for the tests after it. So tests can affect each other. Rule of thumb: each test should only depend on what it set up itself, not on what another test did. (In S20, with a real database, you’ll learn the proper way to give every test a clean start.)
"""

# so we no need import requests and run requests.get?
"""
With requests (Session 10):

import requests

response = requests.get("http://127.0.0.1:8000/todos/1")   # send a real request over the network to a running server

For this to work, you must first start the server in another terminal (uvicorn main:app --reload). If the server isn’t running, you get a connection error.

With TestClient:

from fastapi.testclient import TestClient
from main import app                       # import the app object itself

client = TestClient(app)
response = client.get("/todos/1")          # no "http://127.0.0.1:8000", just the path

No server, no port, no second terminal. TestClient hands the request straight to your app object inside the same Python program.

Analogy:

- requests is like phoning a shop: the shop must be open (server running), and the call travels over the phone line (network).
- TestClient is like walking into the shop’s back office and asking the staff directly. It’s the same question and the same answer, but there’s no phone line, and the shop doesn’t even need to be “open”.

What stays the same: the method names (.get, .post, .put, .delete), json={...} for sending data, and response.status_code / response.json() for checking the answer. That’s why it felt familiar.

When to use which:

	        Use it for
requests	talking to someone else’s API that’s running somewhere (weather API, LLM API in Phase 4)
TestClient	testing your own FastAPI app, quickly and automatically
"""