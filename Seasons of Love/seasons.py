import sys
import inflect
from datetime import date

p = inflect.engine()


def main():
    """Get birthday from user, print duration of minutes in words"""
    dur = calculate(input("Date of Birth: ").strip())
    print(f"{p.number_to_words(dur, andword='').capitalize()} minutes")


def calculate(d):
    """Get a date, return time duration for today in minutes"""

    # Convert "str" date into a date object, check for errors
    try:
        bday = date.fromisoformat(d)
        if not bday <= date.today():
            raise ValueError
    except ValueError:
        pass

    # Calculate duration, return duration in minutes
    else:
        duration = date.today() - bday
        minutes = duration.total_seconds() // 60
        return round(minutes)

    # Exit if found errors
    sys.exit("Invalid date")


if __name__ == "__main__":
    main()
