def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """ returns True if a string meets all requirements and False if it does not."""

    # Initialize Variables and a list of invalid symbols
    number_count = 0
    first = s[0:2]
    invalid = [
        ".", ":", ";", ",", "?", "!", "_", '"',
        "( )", "-", "'""-", "[]", "{}", "/", " "
    ]

    # Validate the length of string
    if 1 < len(s) < 7:
        for i in s:

            # Check for invalid symbols
            # If contain any numbers update number count
            if i in invalid:
                return False
            if i.isdigit():
                number_count += 1

        # Check if first 2 characters are letters
        if first.isalpha():

            # Check if the positions of numbers are valid
            if number_count > 0:

                last = s[-number_count:]

                if last.isdigit():

                    # If zero exist check if it is the last digit
                    if "0" in last:
                        if not s[-number_count] == "0":
                            return True
                        else:
                            return False
                else:
                    return False

            return True
            
    return False


if __name__ == "__main__":
    main()