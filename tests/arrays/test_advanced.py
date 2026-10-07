import pytest

from src.arrays.advanced import kth_largest


@pytest.mark.parametrize(
    "array, k, expected",
    [
        ([3.3, 2.5, 4.0, 12.5, 12.2], 2, 12.2),
        ([3, 5, 6, 10, 12, 8, 3], 1, 12),
        ([17, 100, 24, 12, 6, 3], 3, 17),
        ([3, 5, 6, 10, 12, 8, 3], 5, 5),
        ([-1, -5, -3], 1, -1),
        ([5], 1, 5),
    ],
)
def test_kth_largest(array: list[int], k: int, expected: int) -> None:
    assert kth_largest(array, k) == expected

    with pytest.raises(ValueError):
        kth_largest([2, 7, 5], -2)
    with pytest.raises(ValueError):
        kth_largest([3, 5, 6], 0)
