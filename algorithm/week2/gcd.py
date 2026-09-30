def gcd[T: (int, float)](a: T, b: T) -> T:
    while b != 0:
        a, b = b, a % b

    return a
