import pytest

from bank import value


# Test for greetings with hello


def test_hello():
    assert value("HELLO") == 0
    assert value("hello, how are you?") == 0


# Test for greetings with h


def test_h():
    assert value("How is it going?") == 20
    assert value("Ha 12 people!") == 20


# Test for greetings with no h


def test_no_h():
    assert value("I don't see a hello") == 100
    assert value("And numbers too 1010!") == 100
