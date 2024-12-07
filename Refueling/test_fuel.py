import fuel
import pytest


def test_convert():
    assert fuel.convert("2/3") == 67
    with pytest.raises(ZeroDivisionError):
        fuel.convert("2/0")
    with pytest.raises(ValueError):
        fuel.convert("3")
    with pytest.raises(ValueError):
        fuel.convert("cat/dog")


def test_gauge():
    assert fuel.gauge(67) == "67%"
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"
    assert fuel.gauge(98) == "98%"
    assert fuel.gauge(2) == "2%"
