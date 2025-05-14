"""
This module provides basic arithmetic operations and conversion to binary.
"""


def add(a: int, b: int) -> int:
    """Sum of a and b."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Difference between a and b."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b


def divide(a: int, b: int) -> float:
    """Return the quotient of a divided by b."""
    return a / b


def to_binary(number):
    """Return number converted to binary"""
    if not isinstance(number, int):
        raise TypeError("Input must be integer.")

    if number < 0 or number > 100:
        raise ValueError("Number must be in range 0–100.")
    return bin(number)[2:]
