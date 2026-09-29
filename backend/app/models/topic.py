from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(
        Integer, 
        ForeignKey("courses.id", ondelete = "CASCADE"),
        nullable = False
    )
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    order = Column(Integer, nullable=False, default= 1)

    course = relationship("Course", back_populates="topics")

    resources = relationship(
        "LearningResource",
        back_populates = "topic",
        cascade = "all, delete-orphan"
    )