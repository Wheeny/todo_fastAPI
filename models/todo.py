from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone

class TodoCreate(BaseModel):
    title: str = Field(..., min_length = 1, max_length  = 200)
    description: Optional[str] = None

class TodoUpdate(BaseModel):
    title: str = None
    description: str = None
    completed: bool = None

class Todo(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    title: str
    description: str = None
    completed: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))




