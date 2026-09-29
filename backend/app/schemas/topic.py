from pydantic import BaseModel, ConfigDict

class TopicCreate(BaseModel):
    title: str
    description: str | None = None
    order: int = 1

class TopicResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: str | None = None
    order: int
    model_config = ConfigDict(from_attributes=True)