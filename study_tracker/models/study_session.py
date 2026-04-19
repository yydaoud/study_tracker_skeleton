# models/study_session.py
# Defines the StudySession class.
# Each instance represents one logged study session and should store:
#   - id (int): unique identifier from the database
#   - subject (str): name of the subject studied
#   - duration (float): time studied in minutes or hours
#   - score (float): self-reported or quiz score (0-100)
#   - date (str): date of the session in YYYY-MM-DD format
# May include a __repr__ or __str__ method for clean, readable printing.

class StudySession:

    def __init__(self, subject, duration, score, date, session_id=None):
        self.id = session_id  #unique ID from database
        self.subject = subject  #subject name
        self.duration = duration  #time studied
        self.score = score  #score (0–100)
        self.date = date  #date string (YYYY-MM-DD)

    def __str__(self):
        return f"{self.subject}  {self.duration}  {self.score}  {self.date}"

    def __repr__(self):
        return f"StudySession(id={self.id}, subject='{self.subject}', duration={self.duration}, score={self.score}, date='{self.date}')"
