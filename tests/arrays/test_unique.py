import pytest

from src.arrays import is_unique, remove_duplicates, unique_elements


@pytest.mark.parametrize(
    "array, expected",
    [
        ([3, 1, 5, 63, 6, 36, 3, 1, 0, 4], [5, 63, 6, 36, 0, 4]),
        ([3, 1, 5, 63, 6, 3, 1, 1], [5, 63, 6]),
        ([1, 2, 3, 4, 1, 2, 3, 4], []),
        ([0.2, 0.3, 1.4, 1.4, 5.7], [0.2, 0.3, 5.7]),
        (["3", "5", "6", "3", "1"], ["5", "6", "1"]),
        (["r", "we", "w", "s", "s"], ["r", "we", "w"]),
        (["ali", "ahmad", "ali", "mahmud"], ["ahmad", "mahmud"]),
        ([True, True, False, None], [False, None]),
        ([True, False, None, False, None], [True]),
        ([True, False, None, False, None, True], []),
        ([], []),
    ],
)
def test_unique_elements[T](array: list[T], expected: list[T]) -> None:
    assert unique_elements(array) == expected


@pytest.mark.parametrize(
    "array, expected",
    [
        ([1, 4, 23, 3, 3, 1], [1, 4, 23, 3]),
        ([1.9, 23.1, 3.3, 3.3, 1.9], [1.9, 23.1, 3.3]),
        ([-1, -4, -23, -3, -3, -1], [-1, -4, -23, -3]),
        (["f", "e", "r", "s", "s", "f", "f"], ["f", "e", "r", "s"]),
        (
            ["mac", "linux", "windows", "windows", "android", "windows", "android"],
            ["mac", "linux", "windows", "android"],
        ),
        ([3, 5, -3, 23, 10], [3, 5, -3, 23, 10]),
        ([True, False, True, True, None, False], [True, False, None]),
        ([None, None, None], [None]),
        ([], []),
    ],
)
def test_remove_duplicates[T](array: list[T], expected: list[T]) -> None:
    assert remove_duplicates(array) == expected


@pytest.mark.parametrize(
    "array, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], True),
        ([-1, 1, 2, 3, 4, 5, 6, 7], True),
        ([1, 2, 3, 4, 5, 6, 7, 7], False),
        ([1, 2, 3, 4, 5, 6, 7, 7.1], True),
        (["ali", "osman", "ahmad", "timur"], True),
        (["ali", "osman", "ahmad", "ali"], False),
        (["a", "g", "ds", "se", "we", "ws"], True),
        (["a", "g", "ds", "se", "we", "we"], False),
        ([True, False, None], True),
        ([True, False, False], False),
        ([], True),
        ([0], True),
    ],
)
def test_is_unique[T](array: list[T], expected: bool) -> None:
    assert is_unique(array) == expected
