# Get user input
name = input("camelCase: ")

print("snake_case: ", end="")

# For every letter in the given name
for letter in name:

    # check if uppercased
    # If true print "_"
    if letter.isupper():
        print("_", end="")

    # Print the letter lowercased
    print(letter.lower(), end="")

# print a new line at the end of the loop
print()