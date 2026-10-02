from app.database import SessionLocal
from app.models.question import Question
from app.models.course import Course
from app.models.topic import Topic
from app.question_bank import QUESTIONS


def seed_questions():
    db = SessionLocal()

    try:
        # Prevent duplicate questions if the script is run again
        existing_count = db.query(Question).count()

        if existing_count > 0:
            print(
                f"Questions table already contains "
                f"{existing_count} questions."
            )
            print("No new questions were inserted.")
            return

        inserted = 0

        for question_data in QUESTIONS:

            course_title = question_data["course"]
            topic_title = question_data["topic"]

            # Find course
            course = (
                db.query(Course)
                .filter(Course.title == course_title)
                .first()
            )

            if not course:
                raise Exception(
                    f"Course not found: {course_title}"
                )

            # Find topic under that course
            topic = (
                db.query(Topic)
                .filter(
                    Topic.course_id == course.id,
                    Topic.title == topic_title
                )
                .first()
            )

            if not topic:
                raise Exception(
                    f"Topic not found: "
                    f"{course_title} -> {topic_title}"
                )

            question = Question(
                topic_id=topic.id,
                question_text=question_data["question_text"],
                option_a=question_data["option_a"],
                option_b=question_data["option_b"],
                option_c=question_data["option_c"],
                option_d=question_data["option_d"],
                correct_answer=question_data["correct_answer"],
                difficulty=question_data["difficulty"]
            )

            db.add(question)
            inserted += 1

        db.commit()

        print("\nQuestions seeded successfully!")
        print(f"Total questions inserted: {inserted}")

        # Verification
        print("\nQuestions per topic:")

        courses = (
            db.query(Course)
            .order_by(Course.id)
            .all()
        )

        total = 0

        for course in courses:

            print(f"\n{course.title}")

            topics = (
                db.query(Topic)
                .filter(Topic.course_id == course.id)
                .order_by(Topic.order)
                .all()
            )

            for topic in topics:

                count = (
                    db.query(Question)
                    .filter(Question.topic_id == topic.id)
                    .count()
                )

                print(f"    {topic.title}: {count}")

                total += count

        print(f"\nTOTAL: {total}")

    except Exception as e:
        db.rollback()
        print("\nError while seeding questions:")
        print(e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_questions()