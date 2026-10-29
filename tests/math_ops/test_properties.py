import pytest

from src.math_ops import is_armstrong, is_palindrome, number_type


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
