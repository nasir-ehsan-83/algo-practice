import pytest

from src.math_ops import (
    factorial,
    factorial_recursive,
    factors,
    is_armstrong,
    is_palindrome,
    is_prime,
    number_type,
)


@pytest.mark.parametrize(
    "number, expected",
    [
        (123, "Positive"),
        (65, "Positive"),
        (0.5, "Positive"),
        (3, "Positive"),
        (-123, "Negative"),
        (-12, "Negative"),
        (-0.5, "Negative"),
        (0, "Zero"),
        (0.0, "Zero"),
    ],
)
def test_number_type(number: float, expected: str) -> None:
    assert number_type(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (153, True),
        (370, True),
        (371, True),
        (407, True),
        (1634, True),
        (8208, True),
        (9474, True),
        (1, True),
        (0, True),
        (123, False),
        (100, False),
        (200, False),
        (1234, False),
        (9475, False),
    ],
)
def test_is_armstrong(number: int, expected: bool) -> None:
    assert is_armstrong(number) == expected


import pytest


@pytest.mark.parametrize(
    "number, expected",
    [
        (121, True),
        (1221, True),
        (12321, True),
        (1, True),
        (0, True),
        (7, True),
        (123, False),
        (1234, False),
        (12345, False),
        (10, False),
        (100, False),
        (1231, False),
        (123456789, False),
    ],
)
def test_is_palindrome(number: int, expected: bool) -> None:
    assert is_palindrome(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, False),
        (1, False),
        (-1, False),
        (-7, False),
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (13, True),
        (17, True),
        (97, True),
        (4, False),
        (6, False),
        (9, False),
        (15, False),
        (25, False),
        (49, False),
        (100, False),
        (121, False),
    ],
)
def test_is_prime(number: int, expected: bool) -> None:
    assert is_prime(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, [1]),
        (2, [1, 2]),
        (3, [1, 3]),
        (4, [1, 2, 4]),
        (6, [1, 2, 3, 6]),
        (10, [1, 2, 5, 10]),
        (12, [1, 2, 3, 4, 6, 12]),
        (16, [1, 2, 4, 8, 16]),
        (25, [1, 5, 25]),
        (36, [1, 2, 3, 4, 6, 9, 12, 18, 36]),
        (49, [1, 7, 49]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100]),
    ],
)
def test_factors(number: int, expected: list[int]) -> None:
    assert factors(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (10, 3628800),
        (12, 479001600),
    ],
)
def test_factorial(number: int, expected: int) -> None:
    assert factorial(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (10, 3628800),
        (12, 479001600),
    ],
)
def test_factorial_recursive(number: int, expected: int) -> None:
    assert factorial_recursive(number) == expected
