import datetime
from fastapi import FastAPI, HTTPException, status, Form, Header
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

app = FastAPI()
users = []

class User(BaseModel):
    id = UUID
    created_at: datetime.datetime
    first_name: str = Field(min_length=1)
    last_name: Optional[str]
    phone: str

@app.get('/users')
async def get_all_users():
    return users

@app.get('/users/{user_id}')
async def get_user_by_id(user_id: UUID):
    for user in users:
        if user.id == user_id:
            return user
    raise user_not_found_exception()

@app.post('/users', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    users.append(user)
    return user

@app.post('/users/login')
async def user_login(phone: str=Form(...), password: str=Form(...)):
    return {'phone': {phone}}

@app.put('/users/{user_id}')
async def edit_user(user_id: UUID, user: User):
    for i in range(len(users)):
        if users[i].id == user_id:
            users[i] = user
            return user
    raise user_not_found_exception()

@app.delete('/users/{user_id}')
async def delete_user(user_id: UUID):
    for i in range(len(users)):
        if users[i].id == user_id:
            del users[i]
            return f'User {user_id} deleted'
    raise user_not_found_exception()

def user_not_found_exception():
    return HTTPException(status_code=404, detail='User Not Found')