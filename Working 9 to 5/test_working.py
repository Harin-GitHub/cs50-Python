import pytest
import working


def test_convert():
    assert working.convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert working.convert("10:30 AM to 9 PM") == "10:30 to 21:00"
    assert working.convert("3 PM to 5 AM") == "15:00 to 05:00"
    assert working.convert("1:20 AM to 3:24 AM") == "01:20 to 03:24"
    with pytest.raises(ValueError):
        working.convert("4:30PM to 6AM")
    with pytest.raises(ValueError):
        working.convert("1:20 PM : 3:24 AM")
    with pytest.raises(ValueError):
        working.convert("12:75 AM to 14:24 AM")
