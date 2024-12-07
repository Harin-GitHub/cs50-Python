# Take user input
answer = input("What is the Answer to the Great Question of life, the Universe, and Everything? ")

# Clean user input
answer = answer.lower().replace(" ", "").replace("-", "")

# Check if the answer is "any forty two"
# Print Yes or No
match answer:
    case "fortytwo" | "42":
        print("Yes")
    case _:
        print("No")