import pytest

from src.math_ops import (
    collatz_sequence,
    even_numbers,
    fibonacci,
    list_of_nth_numbers,
    sum_of_nth_natural_number,
)


@pytest.mark.parametrize(
    "number, expected",
    [
        (-5, []),
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (7, [0, 1, 1, 2, 3, 5, 8]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ],
)
def test_fibonacci(number: int, expected: list[int]) -> None:
    assert fibonacci(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, ([1], 0)),
        (2, ([2, 1], 1)),
        (3, ([3, 10, 5, 16, 8, 4, 2, 1], 7)),
        (4, ([4, 2, 1], 2)),
        (5, ([5, 16, 8, 4, 2, 1], 5)),
        (6, ([6, 3, 10, 5, 16, 8, 4, 2, 1], 8)),
        (10, ([10, 5, 16, 8, 4, 2, 1], 6)),
    ],
)
def test_collatz_sequence(
    number: int,
    expected: tuple[list[int], int],
) -> None:
    assert collatz_sequence(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, 0),
        (1, 1),
        (2, 3),
        (3, 6),
        (5, 15),
        (10, 55),
        (100, 5050),
    ],
)
def test_sum_of_nth_natural_number(
    number: int,
    expected: int,
) -> None:
    assert sum_of_nth_natural_number(number) == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 10, [2, 4, 6, 8, 10]),
        (0, 10, [0, 2, 4, 6, 8, 10]),
        (2, 2, [2]),
        (3, 3, []),
        (-5, 5, [-4, -2, 0, 2, 4]),
        (10, 20, [10, 12, 14, 16, 18, 20]),
        (5, 1, []),
    ],
)
def test_even_numbers(
    start: int,
    end: int,
    expected: list[int],
) -> None:
    assert even_numbers(start, end) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (-5, []),
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (3, [0, 1, 2]),
        (5, [0, 1, 2, 3, 4]),
        (10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ],
)
def test_list_of_nth_numbers(
    number: int,
    expected: list[int],
) -> None:
    assert list_of_nth_numbers(number) == expected
