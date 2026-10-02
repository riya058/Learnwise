from app.database import SessionLocal
from app.models.course import Course
from app.models.topic import Topic

courses_data = {
    "Computer Networks": [
        "Network Fundamentals",
        "OSI & TCP/IP Models",
        "Data Link Layer",
        "Network Layer",
        "Transport Layer",
        "Application Layer",
    ],
    "OOPS": [
        "OOP Fundamentals",
        "Classes & Objects",
        "Encapsulation & Abstraction",
        "Inheritance",
        "Polymorphism",
        "Exception Handling",
    ],
    "SQL/DBMS": [
        "DBMS Fundamentals",
        "ER Model",
        "Relational Model & SQL",
        "Normalization",
        "Transactions & Concurrency",
        "Indexing",
    ],
    "Operating Systems": [
        "OS Fundamentals",
        "Processes & Threads",
        "CPU Scheduling",
        "Synchronization & Deadlocks",
        "Memory Management",
        "File Systems",
    ],
}

def seed_topics():
    db = SessionLocal()

    try:
        for course_title, topic_titles in courses_data.items():
            course = (
                db.query(Course)
                .filter(Course.title == course_title)
                .first()
            )
            if not course:
                print(f"Course not found: {course_title}")
                continue

            print(f"\nUpdating Course {course.id}: {course.title}")

            db.query(Topic).filter(
                Topic.course_id == course.id
            ).delete()

            for index, topic_title in enumerate(
                topic_titles,
                start=1
            ):

                topic = Topic(
                    course_id=course.id,
                    title=topic_title,
                    description=f"{topic_title} concepts and fundamentals.",
                    order=index
                )

                db.add(topic)

                print(f"    Added: {topic_title}")

        db.commit()

        print("\nAll courses and topics updated successfully!")

        print("\nFinal database structure:")

        courses = (
            db.query(Course)
            .order_by(Course.id)
            .all()
        )

        for course in courses:

            print(f"\nCourse {course.id}: {course.title}")

            topics = (
                db.query(Topic)
                .filter(Topic.course_id == course.id)
                .order_by(Topic.order)
                .all()
            )

            for topic in topics:
                print(
                    f"     Topic {topic.id}: {topic.title}"
                )

    except Exception as e:

        db.rollback()
        print("Error while seeding:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_topics()