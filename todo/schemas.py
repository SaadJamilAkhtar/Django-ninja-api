from typing import Optional

from ninja import ModelSchema, Schema
from .models import Todo
from datetime import datetime


class TodoSchemaMeta(ModelSchema):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed"]


class TodoSchemaConfig(Schema):
    id: int
    title: str
    description: str | None
    completed: bool
    created_at: datetime  # Convert datetime to string
    updated_at: datetime

    class Config:
        from_attributes = True  # Ensures ORM objects are serialized correctly
        json_encoders = {
            datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S")
        }


class TodoUpdateSchema(Schema):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
