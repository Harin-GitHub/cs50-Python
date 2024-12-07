import pytest
from seasons import calculate


def test_calculate():
    assert calculate("2002-12-26") == 10874880
    assert calculate("1972-10-15") == 26756640
    with pytest.raises(SystemExit):
        calculate("2002/12/26")
    with pytest.raises(SystemExit):
        calculate("cat")
