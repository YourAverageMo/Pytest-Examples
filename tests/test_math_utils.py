import pytest
from math_utils import add, subtract, multiply, divide

# ---------- BASIC NON PARAMETRIZED TEST


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 3) == -3
    assert subtract(3, 3) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 3) == -3
    assert multiply(0, 3) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1, 0)


# ---------- PARAMETRIZED TEST


@pytest.mark.parametrize('a,b,expected', [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


# ---------- SETUP/TEARDOWNS


class TestAdd:

    def setup_method(self):
        print('BEFORE')

    def test_method(self):
        print('DURING')
        assert 0 == 0

    def teardown_method(self):
        print('AFTER')
