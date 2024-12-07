from twttr import shorten


def test_shorten():
    assert shorten("TwiTTer") == "TwTTr"
    assert shorten("What's Your Name?") == "Wht's Yr Nm?"
    assert shorten("BcdFgH") == "BcdFgH"
    assert shorten("HARIN") == "HRN"
    assert shorten("This is CS50") == "Ths s CS50"