def main():

    # Take user input
    greeting = input("Greeting: ").lower().strip()

    # Take the value according to the input
    # Print the reward user get
    reward = value(greeting)
    print(f"${reward}")


def value(greeting):
    """Check if the input starts with helllo or h or otherwise case insensitively. Return the relavant value"""

    # If greeting does start with "h" or "hello" strip them off
    strip_greeting = greeting.lstrip("hello")

    # Check if the length is reduced or not
    # if reduced check "h" or "hello" was stripped
    # Print won dollars
    if len(strip_greeting) == len(greeting):
        return(100)
    elif len(strip_greeting) < len(greeting):
        if len(strip_greeting) < len(greeting) - 4:
            return(0)
        else:
            return(20)


if __name__ == "__main__":
    main()