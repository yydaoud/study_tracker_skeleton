# features/stats.py

import pandas as pd
from database.db_manager import DatabaseManager


def _load_dataframe():
    """Load all sessions from the database into a pandas DataFrame."""
    db = DatabaseManager()
    sessions = db.get_all_sessions()
    if not sessions:
        return pd.DataFrame(columns=["id", "subject", "duration", "score", "date"])
    data = [
        {"id": s.id, "subject": s.subject, "duration": s.duration,
         "score": s.score, "date": s.date}
        for s in sessions
    ]
    return pd.DataFrame(data)


def calculate_average_score(subject):
    """Return the average score for a given subject, or None if no data."""
    df = _load_dataframe()
    filtered = df[df["subject"].str.lower() == subject.lower()]
    if filtered.empty:
        return None
    return round(filtered["score"].mean(), 2)


def get_best_subject():
    """Return the subject with the highest average score."""
    df = _load_dataframe()
    if df.empty:
        return None
    avg_scores = df.groupby("subject")["score"].mean()
    return avg_scores.idxmax()


def get_worst_subject():
    """Return the subject with the lowest average score."""
    df = _load_dataframe()
    if df.empty:
        return None
    avg_scores = df.groupby("subject")["score"].mean()
    return avg_scores.idxmin()


def get_most_studied_subject():
    """Return the subject with the most logged sessions."""
    df = _load_dataframe()
    if df.empty:
        return None
    return df["subject"].value_counts().idxmax()


def session_count_per_subject():
    """Print the number of sessions logged per subject."""
    df = _load_dataframe()
    if df.empty:
        print("No sessions logged yet.")
        return
    counts = df["subject"].value_counts()
    print("\n--- Sessions Per Subject ---")
    for subject, count in counts.items():
        print(f"  {subject}: {count} session(s)")


def display_summary():
    """Print total study time, total sessions, and per-subject breakdowns."""
    df = _load_dataframe()

    print("\n--- Study Summary ---")
    if df.empty:
        print("No sessions logged yet.")
        return

    total_sessions = len(df)
    total_time = df["duration"].sum()
    print(f"Total Sessions : {total_sessions}")
    print(f"Total Study Time: {total_time} minutes ({round(total_time / 60, 1)} hours)")

    print("\n--- Per-Subject Breakdown ---")
    summary = df.groupby("subject").agg(
        sessions=("id", "count"),
        total_minutes=("duration", "sum"),
        avg_score=("score", "mean")
    ).reset_index()

    for _, row in summary.iterrows():
        print(
            f"  {row['subject']}: "
            f"{row['sessions']} session(s), "
            f"{row['total_minutes']} min, "
            f"avg score: {round(row['avg_score'], 1)}"
        )

    best = get_best_subject()
    worst = get_worst_subject()
    print(f"\n🏆 Best Subject  : {best}")
    print(f"⚠️  Needs Work    : {worst}")
