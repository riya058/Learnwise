from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.course import Course
from app.models.topic import Topic 
from app.schemas.topic import TopicCreate, TopicResponse

router = APIRouter(
    prefix="/api/courses/{course_id}/topics",
    tags=["Topics"]
)

@router.post("/", response_model=TopicResponse)
def create_topic(
    course_id: int,
    topic: TopicCreate,
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=404, 
            detail="Course not found"
        )
    
    new_topic = Topic(
        course_id=course_id,
        title=topic.title,
        description=topic.description,
        order=topic.order
    )
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic

@router.get("/", response_model=list[TopicResponse])
def get_topics(
    course_id: int, 
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=404, 
            detail="Course not found"
        )
    
    topics = db.query(Topic).filter(Topic.course_id == course_id).all()
    return topics

@router.get("/{topic_id}", response_model=TopicResponse)
def get_topic(
    course_id: int, 
    topic_id: int, 
    db: Session = Depends(get_db)
):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=404, 
            detail="Course not found"
        )
    
    topic = db.query(Topic).filter(Topic.id == topic_id, Topic.course_id == course_id).first()
    if not topic:
        raise HTTPException(
            status_code=404, 
            detail="Topic not found"
        )
    
    return topic