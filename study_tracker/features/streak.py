# features/streak.py
# Handles study streak tracking logic.
# Responsibilities:
#   - calculate_streak(): look at session dates in the database and compute
#     how many consecutive days the user has studied up to today
#   - display_streak(): print the streak in a user-friendly message
#     e.g., "You're on a 5-day study streak! Keep it going!"
# Should handle edge cases: duplicate sessions on the same day count as 1 day;
# any gap in dates resets the streak back to 0.
