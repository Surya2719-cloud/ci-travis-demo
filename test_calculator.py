"""
Automated Test Suite for Calculator Module.

This test suite is designed for pytest execution in a Continuous Integration
(CI) pipeline using Travis CI. It validates core functionality, edge cases,
and error conditions.
"""

import pytest
from calculator import add, subtract, multiply, divide


# ==============================================================================
# 1. Addition Tests
# ==============================================================================

def test_add_positive_integers():
    """Verify addition of positive integers."""
    assert add(5, 7) == 12
    assert add(100, 250) == 350


def test_add_negative_integers():
    """Verify addition of negative integers."""
    assert add(-4, -6) == -10
    assert add(-50, -50) == -100


def test_add_mixed_sign_integers():
    """Verify addition of positive and negative integers."""
    assert add(10, -3) == 7
    assert add(-15, 20) == 5


def test_add_with_zero():
    """Verify addition with zero as operand."""
    assert add(0, 0) == 0
    assert add(42, 0) == 42
    assert add(0, -99) == -99


def test_add_floating_point_numbers():
    """Verify addition of floating-point numbers."""
    assert add(2.5, 3.1) == pytest.approx(5.6)
    assert add(0.1, 0.2) == pytest.approx(0.3)


# ==============================================================================
# 2. Subtraction Tests
# ==============================================================================

def test_subtract_positive_integers():
    """Verify subtraction of positive integers."""
    assert subtract(10, 4) == 6
    assert subtract(5, 10) == -5


def test_subtract_negative_integers():
    """Verify subtraction involving negative integers."""
    assert subtract(-5, -5) == 0
    assert subtract(-10, -4) == -6
    assert subtract(10, -5) == 15


def test_subtract_with_zero():
    """Verify subtraction involving zero."""
    assert subtract(0, 0) == 0
    assert subtract(15, 0) == 15
    assert subtract(0, 15) == -15


def test_subtract_floating_point_numbers():
    """Verify subtraction with decimals."""
    assert subtract(5.5, 2.2) == pytest.approx(3.3)
    assert subtract(1.0, 0.9) == pytest.approx(0.1)


# ==============================================================================
# 3. Multiplication Tests
# ==============================================================================

def test_multiply_positive_integers():
    """Verify multiplication of positive integers."""
    assert multiply(3, 7) == 21
    assert multiply(12, 12) == 144


def test_multiply_negative_integers():
    """Verify multiplication involving negative numbers."""
    assert multiply(-4, 5) == -20
    assert multiply(6, -3) == -18
    assert multiply(-7, -8) == 56


def test_multiply_with_zero():
    """Verify that multiplying any number by zero yields zero."""
    assert multiply(0, 0) == 0
    assert multiply(100, 0) == 0
    assert multiply(0, -50) == 0


def test_multiply_floating_point_numbers():
    """Verify multiplication with decimals."""
    assert multiply(2.5, 4.0) == pytest.approx(10.0)
    assert multiply(0.5, 0.5) == pytest.approx(0.25)


# ==============================================================================
# 4. Division Tests
# ==============================================================================

def test_divide_positive_numbers():
    """Verify division of positive numbers."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_negative_numbers():
    """Verify division involving negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-9, -3) == 3.0


def test_divide_floating_point_numbers():
    """Verify division with decimal numbers."""
    assert divide(5.5, 0.5) == pytest.approx(11.0)
    assert divide(1.0, 3.0) == pytest.approx(0.3333333333)


def test_divide_by_zero_raises_exception():
    """Verify that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)

    with pytest.raises(ZeroDivisionError):
        divide(-5, 0)

    with pytest.raises(ZeroDivisionError):
        divide(0, 0)


# ==============================================================================
# 5. Type and Input Validation Tests
# ==============================================================================

def test_invalid_input_types_raise_type_error():
    """Verify that non-numeric types raise TypeError."""
    with pytest.raises(TypeError):
        add("10", 5)

    with pytest.raises(TypeError):
        subtract(5, "three")

    with pytest.raises(TypeError):
        multiply(None, 4)

    with pytest.raises(TypeError):
        divide(10, [2])

    with pytest.raises(TypeError):
        add(True, 5)  # Booleans are technically int subclasses in Python, handled cleanly
