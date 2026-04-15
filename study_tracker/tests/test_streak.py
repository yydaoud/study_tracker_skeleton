# tests/test_streak.py
# Unit tests for the streak tracking feature.
# Should test:
#   - calculate_streak() returns 0 when no sessions exist
#   - calculate_streak() returns the correct count for a run of consecutive days
#   - Streak resets correctly to 0 after a gap in study days
#   - Multiple sessions on the same day are treated as a single study day
