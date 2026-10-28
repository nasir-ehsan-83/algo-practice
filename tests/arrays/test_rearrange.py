import pytest

from src.arrays import is_rotation, rearrange_even_odd


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


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ([1, 2, 3], [2, 3, 1], True),
        ([1, 2, 3], [3, 1, 2], True),
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2, 3], [3, 2, 1], False),
        ([1, 2, 3], [1, 3, 2], False),
        ([1, 2, 3], [2, 1, 3], False),
        ([], [], True),
        ([1], [1], True),
        ([1], [2], False),
        ([1, 2, 3], [1, 2], False),
        ([1, 2, 3], [1, 2, 3, 4], False),
        (["a", "b", "c"], ["b", "c", "a"], True),
        (["a", "b", "c"], ["c", "a", "b"], True),
        (["a", "b", "c"], ["a", "c", "b"], False),
    ],
)
def test_is_rotation[T](
    s1: list[T],
    s2: list[T],
    expected: bool,
) -> None:
    assert is_rotation(s1, s2) is expected
