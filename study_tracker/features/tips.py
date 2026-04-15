# features/tips.py
# Provides study tips and external resource suggestions for struggling subjects.
# Responsibilities:
#   - get_tips(subject): return a list of general study tips for the given subject
#   - get_resources(subject): return relevant external resource links for the subject
#     e.g., Khan Academy for math, Purdue OWL for English writing, etc.
#   - display_help_for_weak_subjects(): automatically find the worst subject (via stats.py)
#     and print both tips and resources for it
# Store subject-to-resource mappings in a dictionary at the top of this file.
