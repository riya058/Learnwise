from pydantic import BaseModel

class QuizQuestionResponse(BaseModel):
    question_id: int
    topic_id: int
    question_text: str
    option_a: str
    option_b: str
    option_c: str
    option_d: str

class QuizResponse(BaseModel):
    course_id: int
    questions: list[QuizQuestionResponse]

class QuizAnswer(BaseModel):
    question_id: int
    selected_answer: str

class QuizSubmission(BaseModel):
    course_id: int
    answers: list[QuizAnswer]

class QuizResult(BaseModel):
    attempt_id: int
    course_id: int
    score: int
    total_questions: int
    percentage: float
    correct_answers: int
    incorrect_answers: int