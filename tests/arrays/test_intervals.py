import pytest

from src.arrays import merge_intervals


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
