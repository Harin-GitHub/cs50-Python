import sys


# Check if user input 2 arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

# Exit if not a Python file
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    # Check if the file does exist
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    # Read lines of the file
    # If a valid line update line count
    else:
        lines = file.readlines()
        file.close()
        linecount = 0
        for line in lines:
            line = line.strip()
            if "'''" or '"""' not in line:
                if not line == "" and not line.startswith("#"):
                    linecount += 1

        # Print the line count to user
        print(linecount)