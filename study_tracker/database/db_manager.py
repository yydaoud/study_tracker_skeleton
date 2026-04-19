# database/db_manager.py
# Defines the DatabaseManager class.
# Handles all interactions with the SQLite database (study_tracker.db).
# Responsibilities:
#   - create_table(): create the 'sessions' table if it doesn't already exist
#     Fields: id (PK), subject, duration, score, date
#   - insert_session(study_session): insert a StudySession object into the database
#   - get_all_sessions(): retrieve all rows and return as a list of StudySession objects
#   - get_sessions_by_subject(subject): return all sessions filtered by subject name
#   - delete_session(session_id): remove a session by its id (stretch goal)
# database/db_manager.py

import sqlite3
from models.study_session import StudySession


class DatabaseManager:
    def __init__(self):
        # name of the SQLite database file
        self.db_name = "study_tracker.db"

    #create the sessions table if it doesn't exist (seed.py)
    def create_table(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT,
                duration INTEGER,
                score INTEGER,
                date TEXT
            )
        """)

        conn.commit()
        conn.close()

    # insert a StudySession object into the database
    def insert_session(self, study_session):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO sessions (subject, duration, score, date)
            VALUES (?, ?, ?, ?)
        """, (
            study_session.subject,
            study_session.duration,
            study_session.score,
            study_session.date
        ))

        conn.commit()
        conn.close()

    #get sessions
    def get_all_sessions(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        #get all rows
        cursor.execute("SELECT * FROM sessions")
        rows = cursor.fetchall()

        #convert rows to StudySession object
        sessions = []
        for row in rows:
            session = StudySession(
                subject=row[1],
                duration=row[2],
                score=row[3],
                date=row[4],
                session_id=row[0]
            )
            sessions.append(session)

        conn.close()
        return sessions

    #get sessions filtered by subject
    def get_sessions_by_subject(self, subject):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM sessions WHERE subject = ?
        """, (subject,))

        rows = cursor.fetchall()

        sessions = []
        for row in rows:
            session = StudySession(
                subject=row[1],
                duration=row[2],
                score=row[3],
                date=row[4],
                session_id=row[0]
            )
            sessions.append(session)

        conn.close()
        return sessions

    #delete a session by id
    def delete_session(self, session_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM sessions WHERE id = ?
        """, (session_id,))

        conn.commit()
        conn.close()