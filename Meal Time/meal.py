def main():

    # Get user input
    time = input("What time is it? ")

    # Return time in hours
    # Check for time
    timehours = convert(time)
    if 7 <= timehours <= 8:
        print("breakfast time")
    elif 12 <= timehours <= 13:
        print("lunch time")
    elif 18 <= timehours <= 19:
        print("dinner time")


def convert(time):
    """converts time, to the corresponding number of hours as a float."""

    # Clean input
    time = time.replace(" ", "").rstrip("a.m.")

    # Check If it is p.m, assign hours and minutes into variables
    # Check if it is exactly 12:## p.m.
    # If it is not add 12 to hours or leave 12 be
    if time.endswith("p"):
        hours, minutes = time.rstrip("p").split(":")
        hours, minutes = int(hours), int(minutes)
        if hours != 12:
            hours += 12
        else:
           hours = 12

    # For any other kind of time(i.e: a.m. ##:##) assign hours and minutes into variables
    else:
        hours, minutes = time.split(":")
        hours, minutes = int(hours), int(minutes)

    # Calculate time in hours
    inhours = float(hours + minutes/60)

    # Return purticular hours
    return inhours


if __name__ == "__main__":
    main()