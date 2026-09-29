from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseResponse

router = APIRouter(
    prefix="/api/courses",
    tags=["Courses"]
)

@router.post("/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(
        title = course.title,
        description = course.description
    )
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return new_course

@router.get("/", response_model=list[CourseResponse])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=404, 
            detail="Course not found"
        )
    return course