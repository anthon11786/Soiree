import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional

app = FastAPI()
events = []

class Event(BaseModel):
    id: UUID
    created_at: datetime.datetime
    name: str = Field(min_length=1)
    date: datetime.date
    time: datetime.time
    description: Optional[str]

@app.get('/events')
async def get_all_events():
    return events