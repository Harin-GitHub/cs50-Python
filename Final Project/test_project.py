import re
import pytest
import string
import pandas as pd
from project import encrypt, decrypt, crypt, cipher


def test_encrypt():
    encrypt("Hello", "test_key.csv")
    df = pd.read_csv("test_key.csv")
    assert len(df.axes[0]) + 1 == 26
    assert len(df.axes[1]) == 2


def test_decrypt():
    with pytest.raises(SystemExit) as exit:
        decrypt("Hello", "abcd.csv")
    assert exit.type == SystemExit
    assert exit.value.code == "abcd.csv: File Not found"


def test_crypt():
    tests = [
            "Hello",
            "Hello I'm Harin",
            "  This  is CS50   ",
            "All Blacks: Winners of Rugby World Cup 2023",
            "Messi is the goat!"
    ]
    test_key = "test_key.csv"

    for test in tests:
        test_msg = ""
        test_words = re.split(r"\s", test)

        encryp = encrypt(test, test_key)

        assert len(test_words) == len(encryp)
        assert test_words != encryp

        test_msg = " ".join(encryp)
        
        decryp = decrypt(test_msg, test_key)
        assert test_words == decryp


def test_cipher():
    dict_cipher = cipher()

    rand_letters = [dict_cipher[letter] for letter in dict_cipher]
    test_ciph_dict = [letter for letter in dict_cipher]

    assert sorted(rand_letters) == test_ciph_dict == list(string.ascii_lowercase)
