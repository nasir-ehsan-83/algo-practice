import pytest

from src.math_ops import count_digits, reverse_number, sum_of_digits


@pytest.mark.parametrize(
    "number, expected",
    [
        (123, 3),
        (65, 2),
        (3, 1),
        (-123, 3),
        (-12, 2),
        (323, 3),
        (236236523, 9),
        (-2336236523, 10),
    ],
)
def test_count_digits(number: int, expected: int) -> None:
    assert count_digits(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, 1),
        (12, 21),
        (54, 45),
        (5, 5),
        (111, 111),
        (789, 987),
        (0, 0),
        (3567, 7653),
        (222, 222),
        (-23, -32),
        (-123, -321),
        (-356, -653),
    ],
)
def test_reverse_number(number: int, expected: int) -> None:
    assert reverse_number(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (123, 6),
        (12, 3),
        (234, 9),
        (987, 24),
        (789, 24),
        (-789, 24),
        (-123, 6),
        (-12, 3),
    ],
)
def test_sum_of_digits(number: int, expected: int) -> None:
    assert sum_of_digits(number) == expected
