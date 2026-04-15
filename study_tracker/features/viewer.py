# features/viewer.py
# Handles displaying session data to the user in a readable format.
# Responsibilities:
#   - display_all_sessions(): fetch all sessions from the database and print
#     them in a formatted table (subject, date, duration, score)
#   - display_sessions_by_subject(subject): filter and print sessions for one subject
#   - display_congratulations(): find the most-studied subject (via stats.py)
#     and print a congratulatory message e.g., "You study Math the most - keep it up!"
# Optionally use pandas or the tabulate library for clean table formatting.
