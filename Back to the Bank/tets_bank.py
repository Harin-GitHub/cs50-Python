from bank import value


def test_basic():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("Bye") == 100


def test_advanced():
    assert value("Hello 2 Harin") == 0
    assert value("Hi 2 Harin") == 20
    assert value("Bye 2 Harin") == 100


def test_casesensitive():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("bye") == 100
    assert value("HELLO") == 0
    assert value("HI") == 20
    assert value("BYE") == 100