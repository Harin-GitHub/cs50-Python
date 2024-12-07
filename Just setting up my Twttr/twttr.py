# Get user input
input = input("Input: ")

# Make a list of vowels
vowels = ["a", "e", "i", "o", "u"]

print("Output: ")

# Check for vowels and omit them
for letter in input:
    if letter.lower() in vowels:
        continue
    print(letter, end="")
print()