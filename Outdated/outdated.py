# Initialize a list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Ask user for date till it's acceptable
# if it is break from the loop
while True:

    # Ask for date and validate
    date = input("Date: ").strip().title()

    # Get date, month, year from a format of "MM-DD-YYYY"
    try:
        m, d, y = date.split("/")
        if 0 < int(d) < 32 and 0 < int(m) <13:
            break
    except ValueError:

        # Get date, month, year from a format of "Month DD, YYYY"
        try:
            s, y = date.split(", ")
            month, d = s.split(" ")
            m = months.index(month) + 1
            if 0 < int(d) < 32:
                break
        except ValueError:
            pass

# Print date in the format of "YYYY-MM-DD"
print(f"{y}-{int(m):02}-{int(d):02}")