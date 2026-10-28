def rearrange_even_odd(arr: list[int]) -> list[int]:
    evens: list[int] = []
    odds: list[int] = []

    for num in arr:
        if num % 2 == 0:
            evens.append(num)

        else:
            odds.append(num)

    return evens + odds


def rotate_right[T](arr: list[T], k: int) -> list[T]:
    n = len(arr)
    if n == 0:
        return arr

    k = k % n
    return arr[-k:] + arr[:-k]


def is_rotation[T](s1: list[T], s2: list[T]) -> bool:
    if len(s1) == 0 and len(s2) == 0:
        return True

    if len(s1) != len(s2):
        return False
    if not s1:
        return True

    n = len(s1)
    doubled = s1 + s1
    return any(doubled[i : i + n] == s2 for i in range(n))
