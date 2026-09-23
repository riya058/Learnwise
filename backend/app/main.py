from fastapi import FastAPI

app = FastAPI(
    title="LearnWise API",
    description="AI-Based Personalized Learning Path Recommendation and Adaptive Assessment System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to LearnWise API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }