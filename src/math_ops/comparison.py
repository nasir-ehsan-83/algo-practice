def is_even(n: float) -> bool:
    return n % 2 == 0


def max_of_three[T: (int, float, str)](a: T, b: T, c: T) -> T:
    maximum: T = a
    maximum = max(maximum, b)
    maximum = max(maximum, c)

    return maximum


def min_of_three[T: (int, float, str)](a: T, b: T, c: T) -> T:
    minimum: T = a
    minimum = min(minimum, b)
    minimum = min(minimum, c)

    return minimum
