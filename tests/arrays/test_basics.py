import pytest

from src.arrays import largest_element


@pytest.mark.parametrize(
    "array, expected",
    [
        ([2, 5, 7, 10, 29, 14, 8, 12], 29),
        ([-2, -5, -7, -10, -29, -14, -8, -12], -2),
        ([-1, -20, -13, -14, 0], 0),
        ([10.0, 2.8, 3.2, 1.4, 0], 10.0),
        ([-1.2, -0.3, -13.7, -14.1, 0.0], 0.0),
        ([], None),
    ],
)
def test_largest_element[T: (int, float)](array: list[T], expected: T) -> None:
    assert largest_element(array) == expected
