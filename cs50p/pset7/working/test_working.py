import pytest
from working import convert


# Test for 3+ digit imput
def test_three():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

    with pytest.raises(ValueError):
        convert("9:90 PM to 5:70 AM")


# Test for 1-2 digit imput
def test_one():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("6 PM to 1 AM") == "18:00 to 01:00"
    assert convert("12 AM to 8 PM") == "00:00 to 20:00"

    with pytest.raises(ValueError):
        convert("13 AM to 7 PM")


# Test for invalid input
def test_invalid():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:50 AM 8:43 PM")
