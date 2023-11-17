import pytest

from plates import is_valid

# Test for plates starting with letters


def test_letter_start():
    assert is_valid("88RT9") == False
    assert is_valid("F9302") == False


# Test for plates that contain between 2 and 6 characters


def test_two_six():
    assert is_valid("A") == False
    assert is_valid("FKD7895") == False


# Test for plates with no numbers in the middle


def test_num_middle():
    assert is_valid("RT98GD") == False
    assert is_valid("FK09") == False


# Test for plates with no punctuation


def test_no_punctuation():
    assert is_valid("JT 70") == False
    assert is_valid("NJT:34") == False
