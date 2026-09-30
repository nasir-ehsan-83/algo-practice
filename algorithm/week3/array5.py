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
