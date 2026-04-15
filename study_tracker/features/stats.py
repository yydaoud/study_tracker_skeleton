# features/stats.py
# Contains functions for calculating and displaying study statistics using pandas.
# Responsibilities:
#   - calculate_average_score(subject): return the average score for a given subject
#   - get_best_subject(): return the subject with the highest average score
#   - get_worst_subject(): return the subject with the lowest average score
#   - display_summary(): print total study time, total sessions, and per-subject breakdowns
#   - session_count_per_subject(): print how many sessions have been logged per subject
#   - get_most_studied_subject(): return the subject with the highest session count
# All functions should load data via DatabaseManager and use pandas for analysis.
