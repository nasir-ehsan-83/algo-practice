import pytest

from src.arrays import arr_eq


@pytest.mark.parametrize(
    "array1, array2, expected",
    [
        ([1.0, 20.0, 12.0, 3.0], [1, 20, 12, 3], True),
        ([1, 12, 5, 3], [1, 12, 5, 3], True),
        ([1, 4, 12, 34, 64, 4], [4, 64, 34, 12, 4, 1], False),
        ([1.0, 20.0, 12.0, 3.0], [-1, -20, -12, -3], False),
        ([11, 12, 5, 3], [1, 12, 5, 3], False),
        ([23, 43, 3, 2, 62, 15], [23, 3, 2, 62, 15], False),
    ],
)
def test_arr_eq[T](array1: list[T], array2: list[T], expected: bool) -> None:
    assert arr_eq(array1, array2) == expected
