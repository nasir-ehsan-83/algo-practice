def largest_smallest[T: (int, float)](a: T, b: T, c: T) -> tuple[T, T]:
    largest: T = a
    largest = max(largest, b)
    largest = max(largest, c)

    smallest: T = a

    smallest = min(smallest, b)
    smallest = min(smallest, c)

    return largest, smallest


def largest_element[T: (int, float)](arr: list[T]) -> T | None:
    if not arr:
        return None

    max_val: T = arr[0]
    for num in arr:
        max_val = max(max_val, num)

    return max_val


def smallest_element[T: (int, float)](arr: list[T]) -> T | None:
    if not arr:
        return None

    min_val: T = arr[0]
    for num in arr:
        min_val = min(min_val, num)

    return min_val


def sum_elements(arr: list[int]) -> int:
    total: int = 0

    for num in arr:
        total += num

    return total


def second_largest[T: (int, float)](arr: list[T]) -> float | None:
    if len(arr) < 2:
        return None

    first: float = float("-inf")
    second: float = float("-inf")

    for num in arr:
        if num > first:
            second = first
            first = num

        elif num > second and num != first:
            second = num

    return second
