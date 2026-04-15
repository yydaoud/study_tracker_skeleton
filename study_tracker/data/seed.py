# data/seed.py
# Script for preloading the database with sample data for testing purposes.
# Responsibilities:
#   - Read rows from sample_data.csv using pandas or the csv module
#   - Create a StudySession object for each row in the CSV
#   - Use DatabaseManager.insert_session() to save each session to the database
#   - Should check if the database is already seeded to avoid inserting duplicates
# Run this script independently before testing the app: python data/seed.py
