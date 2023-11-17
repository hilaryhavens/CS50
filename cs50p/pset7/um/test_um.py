import pytest

from um import count


def test_single():
    assert count("um") == 1
    assert count("Um is um") == 2
    assert count("cat") == 0

def test_punctuation():
    assert count("hi um!") == 1
    assert count("Is that an um? no, um") == 2
    assert count("um...") == 1

def test_embed():
    assert count("yummy") == 0
    assert count("umber is pummel") == 0
    assert count("umbra is Um") == 1
