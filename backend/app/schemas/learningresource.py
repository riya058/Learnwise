from pydantic import BaseModel, ConfigDict

class LearningResourceCreate(BaseModel):
    title: str
    description: str | None = None
    resource_type: str
    url: str
    order: int = 1

class LearningResourceResponse(BaseModel):
    id: int
    topic_id: int
    title: str
    description: str | None = None
    resource_type: str
    url: str
    order: int
    model_config = ConfigDict(from_attributes=True)