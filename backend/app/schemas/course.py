from datetime import datetime
from pydantic import BaseModel, ConfigDict

class CourseCreate(BaseModel):
    title: str
    description: str | None = None

class CourseResponse(BaseModel):
    id: int
    title: str
    description: str | None = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)