import sys
import csv
from tabulate import tabulate


# Check if user input 2 arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Exit if not a CSV file
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    # Check if the file does exist
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Print ASCII formatted table to the user
    else:
        reader = csv.DictReader(file)
        print(tabulate(reader, headers="keys", tablefmt="grid"))
        file.close()