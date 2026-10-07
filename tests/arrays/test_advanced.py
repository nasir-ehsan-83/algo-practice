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
def test_kth_largest[T: (int, float, str)](array: list[T], k: int, expected: T) -> None:
    assert kth_largest(array, k) == expected

    with pytest.raises(ValueError):
        kth_largest([2, 7, 5], -2)
    with pytest.raises(ValueError):
        kth_largest([3, 5, 6], 0)
    with pytest.raises(ValueError):
        top_k_freq([3, 5, 6], 4)


@pytest.mark.parametrize(
    "array, k, expected",
    [
        ([4, 5, 3, 7, 1, 9, 4, 8, 3], 2, [4, 3]),
        ([1.0, 2, 7, 8, 3, 7, 1, 9], 2, [7, 1]),
        ([2, 3, 4, 7, 8, 8, 8, 1, 9, 5, 3, 2], 3, [8, 3, 2]),
        ([1.3, 4, 4, 1.3, 6.4, 6.4, 5.2], 3, [6.4, 4, 1.3]),
        ([-1, -2, -7, -8, -3, -7, -1, -9], 2, [-1, -7]),
        ([-4, -4, -6.4, -6.4, -5.2], 2, [-4, -6.4]),
        (["1", "2", "7", "8", "3", "7", "1", "9"], 2, ["7", "1"]),
        (["c", "c", "b", "g", "k", "b", "c", "r"], 2, ["c", "b"]),
        (["cc", "ca", "be", "gt", "gt", "be", "g", "d"], 2, ["gt", "be"]),
    ],
)
def test_top_k_freq[T: (int, float, str)](
    array: list[T], k: int, expected: list[T]
) -> None:
    assert top_k_freq(array, k) == expected

    with pytest.raises(ValueError):
        top_k_freq([4, 5, 4], -2)
    with pytest.raises(ValueError):
        top_k_freq([3, 2, 2], 0)
    with pytest.raises(ValueError):
        top_k_freq([3, 5, 6], 4)
