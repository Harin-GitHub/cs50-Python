from numb3rs import validate


def test_validate():
    assert validate("123.256.455.768") == False
    assert validate("32.1.123.255") == True
    assert validate("1.98.100.156") == True
    assert validate("1.23.79") == False
    assert validate("255.255.255.255") == True
