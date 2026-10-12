def contains[T](arr: list[T], x: T) -> bool:
    for num in arr:
        if num == x:
            return True

    return False


def count_occurrences[T](arr: list[T], x: T) -> int:
    count: int = 0
    for num in arr:
        if num == x:
            count += 1

    return count


def find_missing_number(arr: list[int], N: int) -> int | None:
    n: int = len(arr)

    if not n or n >= N or n < N - 1:
        return None

    if min(arr) <= 0:
        raise ValueError("Array elements should be greater than 0")

    total = N * (N + 1) // 2
    sum_arr = 0

    for num in arr:
        sum_arr += num

    return total - sum_arr
