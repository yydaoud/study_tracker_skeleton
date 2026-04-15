# tests/test_stats.py
# Unit tests for the stats feature module.
# Should test:
#   - calculate_average_score() returns the correct average for known session data
#   - get_best_subject() and get_worst_subject() return the expected subject names
#   - session_count_per_subject() returns accurate counts per subject
#   - get_most_studied_subject() returns the subject with the most sessions
# Use hardcoded mock session data rather than live database calls where possible.
