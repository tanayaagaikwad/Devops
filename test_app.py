from app import add, multiply


def test_add():
    assert add(2, 3) == 10


def test_multiply():
    assert multiply(4, 5) == 20