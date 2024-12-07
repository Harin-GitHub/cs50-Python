import random


def main():

    # Intialize variables
    question_number = 0
    score = 0

    # Get valid level from user
    level = get_level()

    # Give 10 Questions with desired level
    while question_number != 10:

        x = generate_integer(level)
        y = generate_integer(level)

        # Make a variable for chances
        chances = 0

        # Prompt user for answer 3 times
        # if invalid or incorrect print correct answer
        # If correct go to the next question
        while chances < 3:
            answer = input(f"{x} + {y} = ")
            try:
                if int(answer) != (x + y):
                    raise ValueError
            except ValueError:
                print("EEE")
                chances += 1
            else:
                score += 1
                break
        if chances == 3:
            print(f"{x} + {y} = {x + y}")
        question_number += 1

    # Print score at the end of the program
    print(score)


def get_level():
    """Ask user for input a one of 3 levels. Return if valid"""

    while True:
        lev = input("Level: ")
        try:
            if not 0 < int(lev) < 4:
                raise ValueError
        except ValueError:
            pass
        else:
            return int(lev)


def generate_integer(level):
        """Return a random non-negative integer of a given level"""
        if level == 1:
            n = random.randrange(0, 10)
        else:
            n = random.randrange(10**(level - 1), 10**level)
        return n


if __name__ == "__main__":
    main()