import pytest

from src.arrays import intersection, merge_intervals


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[2, 6], [10, 12], [5, 13]], [[2, 13]]),
        ([[0, 2], [1, 4], [5, 9]], [[0, 4], [5, 9]]),
        ([[-8, -6], [-10, -7], [-5, -2]], [[-10, -6], [-5, -2]]),
        (
            [[0.5, 3.2], [3.5, 4.9], [-2.9, 0.5], [-3.2, -5.12]],
            [[-3.2, -5.12], [-2.9, 3.2], [3.5, 4.9]],
        ),
        ([], []),
    ],
)
def test_merge_intervals(intervals: list[list[int]], expected: list[int]) -> None:
    assert merge_intervals(intervals) == expected


@pytest.mark.parametrize(
    "array1, array2, expected",
    [
        ([3, 4, 2], [5, 3, 2], [3, 2]),
        ([6, 4, 2, 10], [5, 3, 2], [2]),
        ([3.0, 4.23, 2.17], [5.39, 3.0, 2.0, 18.1], [3.0]),
        ([-3, 4, -2], [5, 3, -2], [-2]),
        (["a", "d", "g", "w", "e"], ["z", "a", "t", "e"], ["a", "e"]),
        (["ali", "ahmad", "timur"], ["osman", "timur", "mohammad"], ["timur"]),
    ],
)
def test_intersection[T](array1: list[T], array2: list[T], expected: list[T]) -> None:
    assert intersection(array1, array2) == expected
