import random
from sys import exit


def main():

    # Get a valid level from user
    level = ask("Level: ")
    
    # Generate a random integer within the level
    n = random.randint(1, level)

    # Ask user to guess a number
    while True:
        guess = ask("Guess: ")

        # Print as relevant if the number is too large, too small or just right
        if n < guess:
            print("Too large!")
        elif n > guess:
            print("Too small!")
        else:
            exit("Just right!")
        continue


def ask(str):
    """Ask user for input till given an int"""
    
    while True:
        res = input(str)
        res = validate(res)
        if res != False:
            return res 


def validate(lev):
    """Check if user input is an int"""

    try:
        lev = int(lev)
    except ValueError:
        pass
    else:
        if lev > 0:
            return lev
    return False
    

main()