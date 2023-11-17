import pytest

from twttr import shorten

# Test for words without vowels


def test_no_vowels():
    assert shorten("2,578") == "2,578"
    assert shorten("nymph") == "nymph"


# Test for words with vowels


def test_vowels():
    assert shorten("Emoji") == "mj"
    assert shorten("how are you?") == "hw r y?"
