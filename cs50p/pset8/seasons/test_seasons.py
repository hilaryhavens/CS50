import pytest

from seasons import check_birthday

# Tests invalid imput from get_birthday function
def test_check_birthday():
    with pytest.raises(SystemExit):
      check_birthday("3024-89-02")
    with pytest.raises(SystemExit):
      check_birthday("January 7")

