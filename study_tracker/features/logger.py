# features/logger.py

from models.study_session import StudySession
from database.db_manager import DatabaseManager
from utils.helpers import get_today, validate_score, validate_duration, format_date


def prompt_new_session():
    print("\n--- Log a New Study Session ---")

    # Subject
    subject = input("Enter subject name: ").strip()
    while not subject:
        print("Subject cannot be empty.")
        subject = input("Enter subject name: ").strip()

    # Duration
    while True:
        duration_input = input("Enter duration (in minutes): ").strip()
        valid, duration = validate_duration(duration_input)
        if valid:
            break
        print("Invalid duration. Please enter a positive number.")

    # Score
    while True:
        score_input = input("Enter score (0-100): ").strip()
        valid, score = validate_score(score_input)
        if valid:
            break
        print("Invalid score. Please enter a number between 0 and 100.")

    # Date
    date_input = input(f"Enter date (YYYY-MM-DD) [press Enter for today]: ").strip()
    if not date_input:
        date = get_today()
    else:
        date = format_date(date_input)
        while date is None:
            print("Invalid date format. Please use YYYY-MM-DD.")
            date_input = input("Enter date (YYYY-MM-DD): ").strip()
            date = format_date(date_input)

    # Create and save session
    session = StudySession(subject=subject, duration=duration, score=score, date=date)
    db = DatabaseManager()
    db.insert_session(session)

    print(f"\n✅ Session logged: {subject} | {duration} min | Score: {score} | Date: {date}")
    return session
