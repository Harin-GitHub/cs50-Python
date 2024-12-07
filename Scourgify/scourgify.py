import sys
import csv


def main():
    # Check if user input just 2 arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Check if the file does exist
    else:
        try:
            file = open(sys.argv[1])
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

        # Update the file
        else:
            reader = csv.DictReader(file)
            clean(reader, sys.argv[2])
            file.close()


def clean(list, arg):
    """Take two CSV files(one as a list of dictionarie). Return the new file, correctly written"""

    # Create a list to store dictionaries
    after_list = []

    # Split name's two parts
    # Add the corrected name and the house to a dictionary
    # Append every dic to the list
    for dic in list:
        last, first = dic["name"].split(", ")
        after_list.append({"first": first, "last": last, "house": dic["house"]})

    # Write the new file using the list of dictionaries
    # Return the file
    with open(arg, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(
            {"first": updic["first"], "last": updic["last"], "house": updic["house"]}
            for updic in after_list
        )
        return file


if __name__ == "__main__":
    main()
