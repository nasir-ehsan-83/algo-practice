def max_subarray_sum[T: (int, float)](arr: list[T]) -> T | int:
    max_sum: T | int = arr[0] if arr else 0
    current: T | int = arr[0] if arr else 0

    for num in arr[1:]:
        current = max(num, current + num)
        max_sum = max(max_sum, current)

    return max_sum
