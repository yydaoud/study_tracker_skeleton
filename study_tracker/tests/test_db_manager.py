# tests/test_db_manager.py
# Unit tests for the DatabaseManager class.
# Should test:
#   - create_table() successfully creates the 'sessions' table
#   - insert_session() correctly stores a StudySession in the database
#   - get_all_sessions() returns the correct number of records after inserts
#   - get_sessions_by_subject() correctly filters sessions by subject name
# Use an in-memory SQLite database (":memory:") so tests never touch real data.
