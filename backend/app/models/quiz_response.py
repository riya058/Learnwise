from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class QuizResponse(Base):
    __tablename__ = "quiz_responses"

    id = Column(Integer, primary_key=True, index=True)
    attempt_id = Column(Integer, ForeignKey("quiz_attempts.id", ondelete="CASCADE"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    selected_answer = Column(String(1), nullable=False)
    is_correct = Column(Boolean, nullable=False)

    attempt = relationship("QuizAttempt", back_populates="responses")
    question = relationship("Question", back_populates="responses")
    topic = relationship("Topic", back_populates="responses")
    