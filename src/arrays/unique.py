from tables import Any


def unique_elements[T](arr: list[T]) -> list[T]:
    frequency: dict[Any, int] = {}

    for num in arr:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    result = [key for key, value in frequency if value == 1]
    return result


def remove_duplicates[T](arr: list[T]) -> list[T]:
    result: list[T] = []
    seen: set[T] = set()

    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result


def is_unique[T](s: list[T]) -> bool:
    seen: set[T] = set()

    for ch in s:
        if ch in seen:
            return False

        seen.add(ch)

    return True
