import re
import sys
import csv
import string
import random
import argparse


def main(arg) -> None:
    # Check if input contains a '.csv' file
    if not re.search(r".csv$", sys.argv[2]):
        exit("Enter a file of type '.csv'!")

    # Check if message is blank
    while True:
        msg = input("Enter Message to Encrypt/Decrypt: ")
        if msg == "":
            print("Message Was Empty!")
            continue
        else:
            break

    # Funtion correctly as of user's input
    if arg.encrypt:
        cryp_msg = encrypt(msg, arg.encrypt)
    else:
        cryp_msg = decrypt(msg, arg.decrypt)

    # Print encrypted or decrypted message 
    print("Crypted Message: ", end="")
    for word in cryp_msg:
        print(f"{word} ", end="")
    print()


def encrypt(msg: str, file: str) -> list:
    """Encrypt given message. Return encrypted message, store key in given csv file."""

    # generate a key
    key = cipher()

    # encrypt message using key
    encryp_wordlist = crypt(msg, key)
    
    # Write key in given csv file
    with open(file, "w", newline="") as key_file:
        writer = csv.DictWriter(key_file, fieldnames=["letter", "enc_char"])
        writer.writerows({"letter": letter, "enc_char": key[letter]} for letter in key)
    
    return encryp_wordlist


def decrypt(msg: str, key: str) -> list:
    """Decrypt a message using the key stored in given file. Return decrypted message."""

    # Read file containing key, store key in a dictionary
    try:
        file_key = open(key, "r")
    except FileNotFoundError:
        exit(f"{key}: File Not found")
    else:
        reader = csv.reader(file_key)
        key_dic = {row[1]:row[0].strip() for row in reader}
        file_key.close()

    # Decrypt and return message
    return crypt(msg, key_dic) 


def crypt(msg: str, key: dict) -> list:
    """Encrypt or Decrypt a message using key given."""

    # Store words in a list 
    words = re.split(r"\s", msg)

    # Create a list to store crypted message
    cryp_msg = []

    for word in words:
        # Store postions of any capital letters in a word
        upper = [i for i in range(len(word)) if word[i].isupper()]

        word = word.lower()
        cryp_word = ""

        # Crypt each letter in word using key
        for char in word:
            if char.isalpha():
                while char == list(key)[:]:
                    continue
                char = key[char]
            cryp_word += char
        
        # Uppercase crypted letters as of original text
        for n in upper:
            cryp_word = cryp_word[:n] + cryp_word[n].upper() + cryp_word[n + 1:]
        
        # Append each crypted word and return the list
        cryp_msg.append(cryp_word)
    return cryp_msg


def cipher() -> dict:
    """Assign a random letter to each and every letter in alphabet. Return values in a dictionary."""

    key = {}

    # Create two lists containing all alphabet letters, lowercased
    letters = list(string.ascii_lowercase)
    letters_to_select = letters[:]

    # Assign random letter from list_2 to each & every letter in list_1
    for letter in letters:
        # Store each (key, value) in dictionary
        key[letter] = random.choice(letters_to_select)

        # Remove the selected letter from list_2
        letters_to_select.remove(key[letter])

    # Return appended dictionary
    return key


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Encrypt/Decrypt a message",
        usage="%(prog)s --encrypt/--decrypt filename.csv"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--encrypt",help="Name of the file in which the key will be stored(must end with '.csv')")
    group.add_argument("--decrypt",help="Name of the file in which the key is stored(must be of type '.csv')")
    args = parser.parse_args()

    main(args)
