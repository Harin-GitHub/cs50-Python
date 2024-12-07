import re
import sys


def main():
    """Print any YouTube link contained in HTML code"""
    print(parse(input("HTML: ")))


def parse(s):
    """Check and return any matching links"""

    # Check for any matching YouTube link
    match = re.search(
        r'^(<iframe\s).*src="https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)".*(></iframe>)$',
        s,
    )
    # Return any link if found or None otherwise
    if match:
        return f"https://youtu.be/{match.group(3)}"
    return None


if __name__ == "__main__":
    main()
