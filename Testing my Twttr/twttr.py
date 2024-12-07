def main():

    # Get user input
    vowel_word = input("Input: ")

    # Print the relevant vowel omitted str
    output = shorten(vowel_word)
    print(f"Output: {output}")


def shorten(word):
    """Get an input. Omit vowels, return the omitted str"""

    # Create a list of lowercased vowels
    vowels = ["a", "e", "i", "o", "u"]

    # Initialize a variable to store omitted word
    omit_word = ""

    # Check for vowels and omit
    # Append the variable
    for letter in word:
        if letter.lower() in vowels:
            continue
        omit_word += letter
    return omit_word


if __name__ == "__main__":
    main()