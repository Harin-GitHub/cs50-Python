def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """Convert given "string dollars" to floats and Return "float dollars"."""
    
    floatdollars = float(d.lstrip("$"))
    return floatdollars


def percent_to_float(p):
    """Convert given percent to float and Return the float value."""

    floatpercent = int(p.rstrip("%")) / 100
    return floatpercent


main()