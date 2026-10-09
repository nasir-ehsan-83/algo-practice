import pytest

from src.arrays import largest_element, largest_smallest, smallest_element


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


@pytest.mark.parametrize(
    "array, expected",
    [
        ([2, 5, 7, 10, 29, 14, 8, 12], 2),
        ([-2, -5, -7, -10, -29, -14, -8, -12], -29),
        ([-1, -20, -13, -14, 0], -20),
        ([10.0, 2.8, 3.2, 1.4, 0], 0),
        ([-1.2, -0.3, -13.7, -14.1, 0.0], -14.1),
        ([], None),
    ],
)
def test_smallest_element[T: (int, float)](array: list[T], expected: T) -> None:
    assert smallest_element(array) == expected


@pytest.mark.parametrize(
    "first, second, third, expected",
    [
        (34, 12, 23, (34, 12)),
        (-34, -12, -23, (-12, -34)),
        (44.2, 12.4, 23.6, (44.2, 12.4)),
    ],
)
def test_largest_smallest[T: (int, float)](
    first: T, second: T, third: T, expected: tuple[T, T]
) -> None:
    assert largest_smallest(first, second, third) == expected
