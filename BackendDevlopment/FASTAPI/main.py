from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    email: str
    password: str

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


@app.get("/get_demo")
def read_root():
    return {"Hello": "Hello World"}

@app.post('/users')
def create_user(payload: User = Body(...)):
    print(payload)
    return {"message": "User created successfully", "user": payload}

