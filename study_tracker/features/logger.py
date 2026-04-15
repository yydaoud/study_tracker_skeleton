# features/logger.py
# Handles the user-facing flow for logging a new study session.
# Responsibilities:
#   - prompt_new_session(): interactively ask the user for:
#       subject name, duration, score, and date (default to today if left blank)
#   - validate all inputs using helpers from utils/helpers.py
#     (score must be 0-100, duration must be a positive number, date must be valid format)
#   - create and return a StudySession object from the collected inputs
#   - pass the session to DatabaseManager.insert_session() to save it to the database
#   - print a confirmation message after successful logging
