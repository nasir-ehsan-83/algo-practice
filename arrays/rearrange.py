def rearrange_even_odd(arr: list[int]) -> list[int]:
    evens: list[int] = []
    odds: list[int] = []

    for num in arr:
        if num % 2 == 0:
            evens.append(num)

        else:
            odds.append(num)

    return evens + odds


def rotate_right[T](arr: list[T], k: float) -> list[T]:
    n = len(arr)
    if n == 0:
        return arr

    k = k % n
    return arr[-k:] + arr[:-k]


def is_rotation[T](s1: list[T], s2: list[T]) -> bool:
    if len(s1) != len(s2):
        return False

    return s2 in (s1 + s1)
