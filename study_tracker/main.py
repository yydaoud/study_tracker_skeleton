from database.db_manager import DatabaseManager
from features.logger import prompt_new_session
from features.stats import display_summary, get_worst_subject
from features.streak import display_streak
from features.tips import get_tips, get_resources
from utils.helpers import clear_screen, print_separator
from utils.visualizer import prompt_visualization_choice

# This code is written by jim harding


def view_all_sessions():
    db = DatabaseManager()
    sessions = db.get_all_sessions()
    
    # Prints the user's sessions unless there is none.
    print()
    print("All Study Sessions:")
    print()
    if not sessions:
        print("No sessions logged yet.")
        return
    
    print(f"{'Subject': <15} {'Duration': <15} {'Score': <15} {'Date': <15}") # Prints collumn headers
    print()
    for session in sessions: # Prints each session
        print(f"{session.subject: <15} {session.duration: <15} {session.score: <15} {session.date: <15}")
    print()


def get_study_tips(): # Get tips for the weakest subject or allows user to choose what
    # subject they want tips for
    print("Study Tips:")
    print ()
    worst = get_worst_subject() # Gets the user's subject with the lowest avg score.
    # print(f"{worst}")

    if worst is None: # In case the user uses this without logging a session for some reason
        print("No sessions logged yet.")
        return

    # Tells user weakest subject and asks if they want tips for it. If not, they can choose another subject.
    while True:
        print(f"Your weakest subject appears to be: {worst}")
        choice = input("Would you like tips for this subject? (y/n): ").strip().lower()
        if choice == 'y':
            subject = worst
            print()
            break
        if choice == 'n':
            subject = input("Enter the subject name you wish to get tips for: ").strip()
            if not subject:
                print("Invalid subject.")
                print()
                return
            break
        else:
            print("Please enter 'y' or 'n'.")
            print()

    tips = get_tips(subject)
    resources = get_resources(subject)
    # print (f"{tips}")
    #print (f"{resources}")
    
    # Display the tips and resources for the chosen subject
    print(f"Tips for {subject}:")
    for tip in tips:
        print(f"  - {tip}")
    print()
    print(f"Resources for {subject}:")
    for resource in resources:
        print(f"  - {resource}")
    print()


def main_menu(): # Display and handle the main menu.
    while True:
        # This is the opening screen. Here the user picks what they want to do.
        print()
        print("Welcome to the Student Study Tracker! Please choose an option:")
        print()
        print("1. Log a New Study Session")
        print("2. View All Sessions")
        print("3. View Statistics")
        print("4. Check Study Streak")
        print("5. Get Study Tips")
        print("6. Show Charts")
        print("7. Import data")
        print("8. Exit")

        choice = input("Choose an option (1-8): ").strip() # Gets the user input and puts it in "choice".
        print()
        # Depending on the choice, it calls the appropriate function. If the choice is invalid,
        # it shows an error message and loops back to the menu.
        if choice == '1':
            prompt_new_session()
        elif choice == '2':
            view_all_sessions()
        elif choice == '3':
            display_summary()
        elif choice == '4':
            display_streak()
        elif choice == '5':
            get_study_tips()
        elif choice == '6':
            prompt_visualization_choice()
        elif choice == '7':
            print("Thank you for using Study Tracker")
            break
        else:
            print("Enter a number between 1 and 7.")


def start_app():
    db = DatabaseManager()
    db.create_table()
    # print("def start_app working")


if __name__ == "__main__":
    start_app()
    main_menu()
