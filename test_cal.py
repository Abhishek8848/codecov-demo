import pytest
from cal import add, sub, mult, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 3) == -3
    assert sub(-5, -3) == -2

def test_mult():
    assert mult(2, 3) == 6
    assert mult(-2, 3) == -6
    assert mult(0, 3) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-6, 3) == -2
    assert div(5, 2) == 2.5

    # Test division by zero
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        div(5, 0)

if __name__ == "__main__":
    pytest.main()
