import re


def main():
    """Print True or False if the address is valid or not"""
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    """Check validity and return a boolean value"""

    # Check if the address is a valid match
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)

    # Check if each digit is in range
    if match:
        for i in match.groups():
            i = int(i)
            if not 0 <= i <= 255:
                # Return a True or False value
                return False
        return True
    return False


if __name__ == "__main__":
    main()
