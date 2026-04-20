import matplotlib.pyplot as plt
import pandas as pd
from database.db_manager import DatabaseManager


def plot_avg_scores_per_subject(): # Create a bar chart showing average scores for all subjects
    db = DatabaseManager()

    # Gets the sessions or returns if there are none
    sessions = db.get_all_sessions()
    if not sessions:
        print("No study sessions found.")
        return

    data = {
        'subject': [s.subject for s in sessions],
        'score': [s.score for s in sessions]
    }
    df = pd.DataFrame(data)

    # Calculate average scores per subject
    avg_scores = df.groupby('subject')['score'].mean().sort_values(ascending = False)

    # Creates the bar chart
    avg_scores.plot(kind = 'bar')
    plt.title('Average Scores by Subject')
    plt.xlabel('Subject')
    plt.ylabel('Average Score')
    plt.show()


def plot_scores_over_time(subject): # Create a line chart showing scores over time for a specific subject
    db = DatabaseManager()

    # Gets the sessions or returns if there are none
    sessions = db.get_sessions_by_subject(subject)
    if not sessions:
        print(f"No sessions found for subject: {subject}")
        return

    data = {
        'date': [s.date for s in sessions],
        'score': [s.score for s in sessions]
    }
    df = pd.DataFrame(data)

    # Sort by date
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    # Create line chart
    plt.plot(df['date'], df['score'])
    plt.title(f'Scores Over Time for {subject}')
    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.show()


def plot_study_time_over_all_time(): # Create a line chart showing study duration over time for all sessions
    db = DatabaseManager()

    # Gets the sessions or returns if there are none
    sessions = db.get_all_sessions()
    if not sessions:
        print("No study sessions found.")
        return

    data = {
        'date': [s.date for s in sessions],
        'duration': [s.duration for s in sessions]
    }
    df = pd.DataFrame(data)

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    plt.plot(df['date'], df['duration'])
    plt.title('Study Duration Over Time for All Sessions')
    plt.xlabel('Date')
    plt.ylabel('Duration')
    plt.show()


def plot_study_time_over_time_subject(subject): # Create a line chart showing study duration over time for a specific subject
    db = DatabaseManager()

    # Gets the sessions or returns if there are none
    sessions = db.get_sessions_by_subject(subject)
    if not sessions:
        print(f"No sessions found for subject: {subject}")
        return

    data = {
        'date': [s.date for s in sessions],
        'duration': [s.duration for s in sessions]
    }
    df = pd.DataFrame(data)

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    plt.plot(df['date'], df['duration'])
    plt.title(f'Study Duration Over Time for {subject}')
    plt.xlabel('Date')
    plt.ylabel('Duration')
    plt.show()


def prompt_visualization_choice(): # Prompt the user to choose between visualization options
    while True:
        print("Visualization Options:")
        print()
        print("1. Bar graph of average scores for all subjects")
        print("2. Line graph of scores over time for a specific subject")
        print("3. Line graph of study duration over time for all sessions")
        print("4. Line graph of study duration over time for a specific subject")
        print("5. Exit")
        
        # Goes to the appropriate function based of the users input
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            plot_avg_scores_per_subject()
        elif choice == '2':
            subject = input("Enter the subject name: ").strip()
            if subject:
                plot_scores_over_time(subject)
            else:
                print("Subject name cannot be empty.")
        elif choice == '3':
            plot_study_time_over_all_time()
        elif choice == '4':
            subject = input("Enter the subject name: ").strip()
            if subject:
                plot_study_time_over_time_subject(subject)
            else:
                print("Subject name cannot be empty.")
        elif choice == '5':
            break
        else:
            print("Please enter 1, 2, 3, 4, or 5.")