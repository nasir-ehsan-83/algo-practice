def smallest_element[T: (int, float)](arr: list[T]) -> T | None:
    if not arr:
        return None

    min_val: T = arr[0]
    for num in arr:
        min_val = min(min_val, num)

    return min_val
