import pytest

from fuel import convert, gauge


# Test convert for 0, 1, and multiple value fractions, as well as exceptions


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("6/5")
        convert("a/b")


# Test gauge to make sure that E, F, and % are given correct values


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(66) == "66%"
    assert gauge(1) == "E"

