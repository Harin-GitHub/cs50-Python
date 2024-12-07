# Get user input
greeting = input("Greeting: ")

# Force lowercase and strip whitespaces
greeting = greeting.lower().strip()

# If greeting does start with "h" or "hello" strip them off
strip_greeting = greeting.lstrip("hello")

# Check if the length is reduced or not
# if reduced check "h" or "hello" was stripped
# Print won dollars
if len(strip_greeting) == len(greeting):
    print("$100")
elif len(strip_greeting) < len(greeting):
    if len(strip_greeting) < len(greeting) - 4:
        print("$0")
    else:
        print("$20")