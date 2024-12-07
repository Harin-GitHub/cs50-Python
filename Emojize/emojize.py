from emoji import emojize

# Get input from user and print emojized
input = input("Input: ").strip().lower()
print(emojize(input, language = "alias"))