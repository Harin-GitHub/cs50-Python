# TODO
from cs50 import get_int


# Draw for a given input
def draw():
    h = get()
    i = 1
    while i <= h:
        j = i+1

        # Align lines exept for the last
        if j <= h:
            print(" "*(h-j), "#"*i, "", "#"*i, end="")

        # Print last row without any spaces in beginning
        else:
            print("#"*i, "", "#"*i, end="")

        # Go to a new line for every i
        print()
        i += 1


# Validate and get the input from user
def get():
    while True:
        n = get_int("Height: ")
        if n > 0 and n < 9:

            return n


draw()