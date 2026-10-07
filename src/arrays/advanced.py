def max_subarray_sum[T: (int, float)](arr: list[T]) -> T | int:
    max_sum: T | int = arr[0] if arr else 0
    current: T | int = arr[0] if arr else 0

    for num in arr[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)

    return max_sum


def kth_largest[T: (int, float)](arr: list[T], k: int) -> T:
    n: int = len(arr)
    if not 1 <= k <= n:
        raise ValueError(f"k must be in [1, {n}], got {k}")

    a: list[T] = arr.copy()
    for i in range(k):
        max_idx: int = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

    return a[k - 1]


def top_k_freq[T](arr: list[T], k) -> list[T]:
    freq: dict[T, int] = {}

    for n in arr:
        freq[n] = freq.get(n, 0) + 1

    freq_items: list[tuple[T, int]] = list(freq.items())
    freq_items.sort(key=lambda x: x[1], reverse=True)

    return [item[0] for item in freq_items[:k]]
