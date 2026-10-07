import pytest

from src.arrays import kth_largest, top_k_freq


@pytest.mark.parametrize(
    "array, k, expected",
    [
        ([3.3, 2.5, 4.0, 12.5, 12.2], 2, 12.2),
        ([3, 5, 6, 10, 12, 8, 3], 1, 12),
        ([17, 100, 24, 12, 6, 3], 3, 17),
        ([3, 5, 6, 10, 12, 8, 3], 5, 5),
        ([-1, -5, -3], 1, -1),
        ([5], 1, 5),
        (["1", "2", "7", "8", "3", "7", "1", "9"], 3, "7"),
        (["c", "c", "b", "g", "k", "b", "c", "r"], 2, "k"),
        (["cc", "a", "be", "gt", "d"], 4, "be"),
    ],
)
def test_kth_largest[T: (int, float)](array: list[T], k: int, expected: T) -> None:
    assert kth_largest(array, k) == expected

    with pytest.raises(ValueError):
        kth_largest([2, 7, 5], -2)
    with pytest.raises(ValueError):
        kth_largest([3, 5, 6], 0)
    with pytest.raises(ValueError):
        top_k_freq([3, 5, 6], 4)
