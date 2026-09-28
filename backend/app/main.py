from app.routes import auth
from app.database import Base, engine
from app.models import user

from fastapi import FastAPI
from sqlalchemy import text

app = FastAPI(
    title="LearnWise API",
    description="AI-Based Personalized Learning Path Recommendation and Adaptive Assessment System",
    version="1.0.0"
)
app.include_router(auth.router)

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