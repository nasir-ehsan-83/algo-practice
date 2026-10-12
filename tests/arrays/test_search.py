import pytest

from src.arrays import contains, count_occurrences


@pytest.mark.parametrize(
    "array, element, expected",
    [
        ([1, 4, 6, 23, 7, 6, 3], 3, True),
        ([-1, -4, -6, -23, -7, -6, -3], 3, False),
        ([-1, -4, -6, -23, -7, -6, -3], -3, True),
        ([1.0, 4.4, 6.0, 23.1, 7.3, 6.8], 7.3, True),
        (["1.0", "4.4", " 6.0", "23.1", "7.3", "6.8"], "7.3", True),
        (["1.0", "4.4", " 6.0", "23.1", "7.3", "6.8"], 7.3, False),
        (["a", "g", "df", "er", "w", "GT"], "er", True),
        (["ali", "omer", "ahmad", "osman"], "ali", True),
        (["ali", "omer", "ahmad", "osman"], "ila", False),
        ([True, False, True, False], False, True),
        ([True, True, True], False, False),
        ([True, False, None], None, True),
        ([], None, False),
        ([], 0, False),
    ],
)
def test_contains[T](array: list[T], element: T, expected: bool) -> None:
    assert contains(array, element) == expected


@pytest.mark.parametrize(
    "array, element, expected",
    [
        ([3, 5, 2, 6, 2, 6, 10, 4], 6, 2),
        ([-2, -6, -2, -6, -10, -6, -2], -2, 3),
        ([3, 5, 2, 6, 2, 6, 10, 6, 2], 2, 3),
        ([-3, -5, -2, -6, -2, -6, -10], -7, 0),
        ([3, 5, 2, 6, 2, 6, 10, 6, 2], 7, 0),
        (["ali", "omer", "ahmad", "osman"], "ali", 1),
        (["ali", "omer", "ahmad", "osman"], "mahmud", 0),
        (["ali", "omer", "ahmad", "osman"], None, 0),
        ([True, True, True, True], False, 0),
        ([True, False, True, False], False, 2),
        ([None, False, True, None], None, 2),
    ],
)
def test_count_occurrences[T](array: list[T], element: T, expected: int) -> None:
    assert count_occurrences(array, element) == expected
