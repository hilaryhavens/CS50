import pytest

from numb3rs import validate

# Test for valid IP addresses


def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("1.23.45.183") == True
    assert validate("255.255.255.255") == True


# Test for invalid IP addresses


def test_invalid():
    assert validate("0.1.2") == False
    assert validate("234.555.33.50") == False
    assert validate("cat") == False
