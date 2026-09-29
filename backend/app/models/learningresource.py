from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class LearningResource(Base):
    __tablename__ = "learning_resources"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(
        Integer,
        ForeignKey("topics.id", ondelete="CASCADE"),
        nullable=False
    )
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    resource_type = Column(String(50), nullable=False)
    url = Column(String(255), nullable=False)
    order = Column(Integer, nullable=False, default=1)

    topic = relationship("Topic", back_populates="resources")