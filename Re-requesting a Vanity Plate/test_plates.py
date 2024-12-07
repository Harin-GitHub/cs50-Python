from plates import is_valid


def test_beginning():
    assert is_valid("123ABC") == False
    assert is_valid("A23BCD") == False
    assert is_valid("A1BCDE") == False
    assert is_valid("123456") == False
    assert is_valid("ABC123") == True


def test_length():
    assert is_valid("A") == False
    assert is_valid("ABC12DE") == False
    assert is_valid("AB") == True
    assert is_valid("ABC123") == True


def test_numbers():
    assert is_valid("ABC012") == False
    assert is_valid("A0B1C2") == False
    assert is_valid("AB12CD") == False
    assert is_valid("AB1234") == True
    assert is_valid("ABCD12") == True
    assert is_valid("ABC120") == True
    assert is_valid("ABC102") == True


def test_periods():
    assert is_valid("ABC.20") == False
    assert is_valid("ABC12!") == False
    assert is_valid("@ABC12") == False
    assert is_valid("AB_120") == False
    assert is_valid("(AB12)") == False