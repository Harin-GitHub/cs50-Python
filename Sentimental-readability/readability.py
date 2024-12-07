import cs50

# Get user input
original_text = cs50.get_string("Text: ")

# Validating user input
strip_text = original_text.strip()
text = " ".join(strip_text.split())


if " " in text:

    # Count words
    word_count = 1

    for i in text:
        if i == " ":
            word_count += 1

    # Count letters
    letter_count = 0

    for j in text:
        if j.isalpha():
            letter_count += 1

    # Count sentences
    sentence_count = 0

    for z in text:
        if z == "." or z == "!" or z == "?":
            sentence_count += 1

    # Get the average
    L = (letter_count / word_count) * 100
    S = (sentence_count / word_count) * 100

    # Applying Coleman-Liau index
    X = round((0.0588 * L) - (0.296 * S) - 15.8)

    if X > 0:
        if X < 16:
            print(f"Grade", X)
        else:
            print("Grade 16+")
    else:
        print("Before Grade 1")

else:
    print("No enough words")