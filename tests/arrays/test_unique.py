import pytest

from src.arrays import unique_elements


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
