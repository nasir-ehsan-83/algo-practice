import pytest

from src.arrays import rearrange_even_odd


@pytest.mark.parametrize(
    "array, expected",
    [
        ([3, 4, 6, 12, 3, 6, 2, 7], [4, 6, 12, 6, 2, 3, 3, 7]),
        ([12, 6, 10, 24, 3, 13, 19], [12, 6, 10, 24, 3, 13, 19]),
        ([3, 19, 13, 21, 24, 16, 32], [24, 16, 32, 3, 19, 13, 21]),
        ([-3, -4, -12, -3, -2, -7], [-4, -12, -2, -3, -3, -7]),
        ([], []),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
    ],
)
def test_rearrange_even_odd(array: list[int], expected: list[int]) -> None:
    assert rearrange_even_odd(array) == expected
