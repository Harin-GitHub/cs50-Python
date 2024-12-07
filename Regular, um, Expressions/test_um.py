from um import count


def test_count():
    assert count("I'm, um, Harin") == 1
    assert count("Drum... drum") == 0
    assert count("Um, can you say 'um'") == 2
    assert count("You're um beautiful") == 1
    assert count("#Um") == 1
