import re
import sys


def main():
    """Print the count of 'um's in input string"""
    print(count(input("Text: ").strip()))


def count(s):
    """Match 'um's in string and return the count"""
    matches = re.findall(r"\b[Uu][Mm]\b", s)
    return len(matches)


if __name__ == "__main__":
    main()
