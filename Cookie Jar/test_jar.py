import pytest
from jar import Jar


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    jar = Jar(15)
    assert jar.capacity == 15
    with pytest.raises(ValueError):
        jar = Jar(-7)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    assert jar.deposit(4) == None
    with pytest.raises(ValueError):
        jar.deposit(9)
    jar = Jar(7)
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar(12)
    jar.deposit(8)
    assert jar.withdraw(4) == None
    with pytest.raises(ValueError):
        jar.withdraw(10)
    jar = Jar(7)
    jar.deposit(4)
    with pytest.raises(ValueError):
        jar.withdraw(5)
