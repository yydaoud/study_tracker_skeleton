# features/streak.py

from datetime import date, timedelta
from database.db_manager import DatabaseManager


def calculate_streak():
    """
    Calculate how many consecutive days the user has studied up to today.
    Duplicate sessions on the same day count as 1. Any gap resets the streak to 0.
    """
    db = DatabaseManager()
    sessions = db.get_all_sessions()

    if not sessions:
        return 0

    # Get unique study dates as date objects, sorted descending
    unique_dates = sorted(
        set(date.fromisoformat(s.date) for s in sessions),
        reverse=True
    )

    today = date.today()

    # Streak must include today or yesterday to be active
    if unique_dates[0] < today - timedelta(days=1):
        return 0

    streak = 0
    expected = unique_dates[0]  # Start from the most recent date

    for study_date in unique_dates:
        if study_date == expected:
            streak += 1
            expected -= timedelta(days=1)
        elif study_date < expected:
            break  # Gap found, stop counting

    return streak


def display_streak():
    """Print the current study streak in a friendly message."""
    streak = calculate_streak()

    print("\n--- Study Streak ---")
    if streak == 0:
        print("No active streak. Study today to start one! 💪")
    elif streak == 1:
        print("🔥 You studied today — that's day 1 of your streak! Keep going!")
    else:
        print(f"🔥 You're on a {streak}-day study streak! Keep it going!")
