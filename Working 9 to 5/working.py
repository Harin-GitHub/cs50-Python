import re
import sys


def main():
    """Get time in 12 hour format and print in 24 hour format"""
    print(convert(input("Hours: ").strip()))


def convert(s):
    """Check validity and convert the format"""
    times = []
    # Dividing the two times, check each one's validity
    time = s.split(" to ")
    for i in time:
        match = re.fullmatch(r"(\d+)(:([0-5][0-9]))?\s(AM|PM)", i)
        if match:
            # Extract the hours
            hour = int(match.group(1))
            # Check if hours are in range
            if hour <= 12:
                if "PM" in i and hour != 12:
                    hour += 12
                if hour == 12 and "AM" in i:
                    hour = 0
                # Append corrected hours to a list
                times.append(f"{hour:02}")
            else:
                raise ValueError
            # Check for minutes
            if match.group(3) != None:
                # Check if minutes meet the range
                if int(match.group(3)) <= 60:
                    minutes = match.group(3)
                    # Append the list with minutes
                    times.append(minutes)
                else:
                    raise ValueError
            else:
                times.append(f"{0:02}")
        else:
            raise ValueError
    # Return corrected time format
    return f"{times[0]}:{times[1]} to {times[2]}:{times[3]}"


if __name__ == "__main__":
    main()
