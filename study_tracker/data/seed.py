# data/seed.py
# Script for preloading the database with sample data for testing purposes.
# Responsibilities:
#   - Read rows from sample_data.csv using pandas or the csv module
#   - Create a StudySession object for each row in the CSV
#   - Use DatabaseManager.insert_session() to save each session to the database
#   - Should check if the database is already seeded to avoid inserting duplicates
# Run this script independently before testing the app: python data/seed.py

import pandas as pd



import pandas as pd

from database.db_manager import DatabaseManager
from models.study_session import StudySession

dbManager = DatabaseManager()
dbManager.create_table() #calls create_table to make sure a table gets created

#checks for existing data and prevents from adding twice
if len(dbManager.get_all_sessions()) > 0:
    print("Database already seeded.")
else:
    df = pd.read_csv("data/sample_data.csv")


    #loop through each row and create object for each row
    for row in df.itertuples(index=False):
        session = StudySession(
            subject=row.subject,
            duration=int(row.duration),
            score=int(row.score),
            date=row.date
        )
        dbManager.insert_session(session)

    print("Database seeded successfully.")




