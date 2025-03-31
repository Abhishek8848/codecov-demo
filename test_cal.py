import pytest
from cal import add, sub, mult, div

# ✅ Test Addition: Extreme Cases
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(999999999, 1) == 1000000000  # Large numbers
    assert add(-999999999, -1) == -1000000000  # Large negatives
    assert add(1e18, 1) == 1e18 + 1  # Edge case: Very large floating-point number

# ✅ Test Subtraction: Extreme Cases
def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 3) == -3
    assert sub(-5, -3) == -2
    assert sub(999999999, 1) == 999999998  # Large numbers
    assert sub(-999999999, -1) == -999999998  # Large negatives
    assert sub(1e18, 1) == 1e18 - 1  # Large floating-point

# ✅ Test Multiplication: Edge Cases & Overflow Risks
def test_mult():
    assert mult(2, 3) == 6
    assert mult(-2, 3) == -6
    assert mult(0, 3) == 0
    assert mult(999999999, 999999999) == 999999998000000001  # Large numbers
    assert mult(-999999999, 999999999) == -999999998000000001  # Large negatives
    assert mult(1e9, 1e9) == 1e18  # Floating-point precision test

# ✅ Test Division: Critical Cases
def test_div():
    assert div(6, 3) == 2
    assert div(-6, 3) == -2
    assert div(5, 2) == 2.5
    assert div(999999999, 1) == 999999999  # Large number division
    assert div(-999999999, -1) == 999999999  # Large negative number division
    assert div(1e18, 1) == 1e18  # Large floating-point

    # Division by zero should raise an error
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        div(5, 0)

# ✅ Test Floating-Point Precision Issues
def test_floating_point_precision():
    assert div(1, 3) == pytest.approx(0.333333, rel=1e-9)  # Higher precision tolerance

# ✅ Test Negative and Zero Edge Cases
def test_negatives_and_zero():
    assert sub(0, -5) == 5
    assert mult(0, -5) == 0
    assert add(-5, 5) == 0
    assert div(-10, -2) == 5

# ✅ New: Test Type Errors (Invalid Input)
def test_invalid_inputs():
    with pytest.raises(TypeError):
        add("a", 5)
    with pytest.raises(TypeError):
        sub(None, 5)
    with pytest.raises(TypeError):
        mult(5, "b")
    with pytest.raises(TypeError):
        div(5, {})

# ✅ New: Test Division by Negative Number
def test_negative_division():
    assert div(10, -2) == -5
    assert div(-10, -2) == 5
    assert div(-10, 2) == -5

# ✅ New: Test Large Float Multiplication
def test_large_float_multiplication():
    assert mult(1.5e308, 2) == pytest.approx(3e308)  # Edge case: Near float overflow

# ✅ New: Test Adding Large Floating Numbers
def test_large_float_addition():
    assert add(1.7e308, 1.7e308) == pytest.approx(3.4e308)  # Edge case: Near float overflow

if __name__ == "__main__":
    pytest.main()  # pragma: no cover
