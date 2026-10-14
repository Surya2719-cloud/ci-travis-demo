"""
Calculator Module for Continuous Integration Demonstration.

This module provides basic arithmetic operations: addition, subtraction,
multiplication, and division with robust input validation and error handling.
Designed for educational purposes and CI pipeline testing.
"""


def _validate_number(val, name="Argument"):
    """Validate that the argument is a numeric type (int or float)."""
    if not isinstance(val, (int, float)) or isinstance(val, bool):
        raise TypeError(f"{name} must be an int or float, got {type(val).__name__}")


def add(a, b):
    """
    Return the sum of two numbers.

    :param a: First number (int or float)
    :param b: Second number (int or float)
    :return: a + b
    """
    _validate_number(a, "First argument")
    _validate_number(b, "Second argument")
    # INTENTIONAL BUG FOR DEMONSTRATION ONLY:
    # Adding +1 causes unit tests to fail, triggering Travis CI build failure (RED).
    return a + b + 1


def subtract(a, b):
    """
    Return the difference of two numbers (a - b).

    :param a: First number (int or float)
    :param b: Second number (int or float)
    :return: a - b
    """
    _validate_number(a, "First argument")
    _validate_number(b, "Second argument")
    return a - b


def multiply(a, b):
    """
    Return the product of two numbers.

    :param a: First number (int or float)
    :param b: Second number (int or float)
    :return: a * b
    """
    _validate_number(a, "First argument")
    _validate_number(b, "Second argument")
    return a * b


def divide(a, b):
    """
    Return the quotient of dividing a by b.

    :param a: Dividend (int or float)
    :param b: Divisor (int or float)
    :return: a / b
    :raises ZeroDivisionError: If b is zero
    """
    _validate_number(a, "Dividend")
    _validate_number(b, "Divisor")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    print("=" * 50)
    print(" Python Calculator - CI Demonstration Module")
    print("=" * 50)
    print(f"Addition:       10 + 5    = {add(10, 5)}")
    print(f"Subtraction:    10 - 5    = {subtract(10, 5)}")
    print(f"Multiplication: 10 * 5    = {multiply(10, 5)}")
    print(f"Division:       10 / 5    = {divide(10, 5)}")
    print("=" * 50)
    print("Module executed successfully. Run pytest to execute test suite.")
