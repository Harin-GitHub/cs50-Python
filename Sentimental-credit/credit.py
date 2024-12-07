from cs50 import get_string


def check():

    # Checking for card type
    number = validate()
    length = len(number)
    l = int(length)

    if l == 15:
        if int(number[:2]) in (int(34), int(37)):
            print("AMEX")
        else:
            print("INVALID")

    elif l == 13:
        if int(number[0]) == 4:
            print("VISA")
        else:
            print("INVALID")

    elif l == 16:
        if int(number[0]) == 4:
            print("VISA")
        elif int(number[:2]) in (int(51), int(52), int(53), int(54), int(55)):
            print("MASTERCARD")
        else:
            print("INVALID")

    else:
        print("INVALID")


def validate():

    N = get_string("Number: ")

    # Removing spaces in user input
    n = N.replace(" ", "")

    # Every "muliplyed by 2" digts
    # Store values of digits multiplyed by 2 in a list
    # Store in string type
    int_digits = []
    str_digits = []

    x = len(n) - 2
    while x >= 0:
        int_digit = int(n[x])*2

        # Addind to a list of ints
        int_digits.append(int_digit)
        x -= 2

    for i in int_digits:
        str_digit = str(i)

        # Converting to list of strings
        str_digits.append(str_digit)

    total = 0
    sum = 0
    for z in str_digits:
        if len(z) == 2:
            sum = int(z[0]) + int(z[1])

        else:
            sum = int(z)
        total += sum

    # Every other digits
    int_otherdigits = []

    y = len(n) - 1
    while y >= 0:
        otherdigits = int(n[y])
        int_otherdigits.append(otherdigits)
        y -= 2

    # Last validation
    valid_sum = 0

    for b in int_otherdigits:
        valid_sum += b

    valid_total = total + valid_sum

    if int(str(valid_total)[-1]) == 0:
        return (n)
    else:
        print("INVALID")
        exit()


check()