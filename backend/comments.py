import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()
comments = []

class Comment(BaseModel):
    id: UUID
    created_at: datetime.datetime
    content: str = Field(min_length=1)
    