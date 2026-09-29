from app.routes import auth
from app.database import Base, engine
from app.models import user
from app.models.course import Course
from app.models.topic import Topic
from app.models.learningresource import LearningResource
from app.routes.course import router as course_router
from app.routes.topic import router as topic_router
from app.routes.learningresource import router as learningresource_router

from fastapi import FastAPI
from sqlalchemy import text

app = FastAPI(
    title="LearnWise API",
    description="AI-Based Personalized Learning Path Recommendation and Adaptive Assessment System",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(course_router)
app.include_router(topic_router)
app.include_router(learningresource_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Welcome to LearnWise API"
    }


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }