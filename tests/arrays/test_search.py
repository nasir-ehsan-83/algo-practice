import pytest

from src.arrays import contains


@pytest.mark.parametrize(
    "array, element, expected",
    [
        ([1, 4, 6, 23, 7, 6, 3], 3, True),
        ([-1, -4, -6, -23, -7, -6, -3], 3, False),
        ([-1, -4, -6, -23, -7, -6, -3], -3, True),
        ([1.0, 4.4, 6.0, 23.1, 7.3, 6.8], 7.3, True),
        (["1.0", "4.4", " 6.0", "23.1", "7.3", "6.8"], "7.3", True),
        (["1.0", "4.4", " 6.0", "23.1", "7.3", "6.8"], 7.3, False),
        ([], 0, False),
        ([], None, False),
    ],
)
def test_contains[T](array: list[T], element: T, expected: bool) -> None:
    assert contains(array, element) == expected
