# main.py
# Entry point for the Student Study Tracker application.
# Responsibilities:
#   - Initialize the database on first run by calling DatabaseManager.create_table()
#   - Display the main menu in a loop with options such as:
#       1. Log a new study session
#       2. View all sessions
#       3. View statistics and summaries
#       4. View study streak
#       5. Get tips for weak subjects
#       6. Show charts (optional)
#       7. Exit
#   - Route each menu choice to the appropriate function from the features/ modules
#   - Keep the loop running until the user selects Exit
