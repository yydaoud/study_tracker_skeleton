# Student Study Tracker and Performance Analyzer

A Python CLI app to log study sessions, analyze performance, and get subject-specific tips.

## Project Structure

```
study_tracker/
├── main.py                    # Entry point and main menu loop
├── requirements.txt           # Python dependencies
├── models/
│   └── study_session.py       # StudySession class
├── database/
│   └── db_manager.py          # DatabaseManager (SQLite operations)
├── features/
│   ├── logger.py              # Log a new study session
│   ├── viewer.py              # Display sessions and congratulations
│   ├── stats.py               # Statistics and performance analysis
│   ├── streak.py              # Consecutive study day tracking
│   └── tips.py                # Tips and external resources
├── utils/
│   ├── helpers.py             # Shared utility functions
│   └── visualizer.py          # Optional matplotlib charts (stretch goal)
├── data/
│   ├── sample_data.csv        # Sample sessions for testing
│   └── seed.py                # Script to preload the database
└── tests/
    ├── test_db_manager.py
    ├── test_stats.py
    └── test_streak.py
```

## Setup

```bash
pip install -r requirements.txt
python data/seed.py     # Optional: preload sample data
python main.py          # Run the app
```
