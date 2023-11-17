import pytest

from jar import Jar

#Either before or after you implement jar.py, additionally implement,
#in a file called test_jar.py, four or more functions that collectively test your implementation of Jar thoroughly,
#each of whose names should begin with test_ so that you can execute your tests with: pytest test_jar.py

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.cookies == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(10)
    with pytest.raises(ValueError):
      jar.deposit(2)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
      jar.withdraw(10)