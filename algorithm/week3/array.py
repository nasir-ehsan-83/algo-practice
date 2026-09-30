def largest_element[T: (int, float)](arr: list[T]) -> T | None:
    if not arr:
        return None

    max_val: T = arr[0]
    for num in arr:
        max_val = max(max_val, num)

    return max_val
