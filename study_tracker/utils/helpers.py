# utils/helpers.py

import os
from datetime import date


def get_today(): #Return today's date as a YYYY-MM-DD string.
    return date.today().isoformat()


def format_date(date_str): #Parse and validate a date string. Returns YYYY-MM-DD string if valid, else None.
    try:
        parsed = date.fromisoformat(date_str.strip())
        return parsed.isoformat()
    except ValueError:
        return None


def validate_score(value): #Check that value is a number between 0 and 100. Returns (True, float) if valid, (False, None) otherwise.
    try:
        score = float(value)
        if 0 <= score <= 100:
            return True, score
        return False, None
    except (ValueError, TypeError):
        return False, None


def validate_duration(value): #Check that value is a positive number. Returns (True, float) if valid, (False, None) otherwise.
   
    try:
        duration = float(value)
        if duration > 0:
            return True, duration
        return False, None
    except (ValueError, TypeError):
        return False, None


def clear_screen(): #Clear the terminal screen.
    os.system("cls" if os.name == "nt" else "clear")


def print_separator(char="-", length=40): #Print a visual dividing line.
    print(char * length)
