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
