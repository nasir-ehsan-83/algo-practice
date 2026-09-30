from gcd import gcd  # reuse gcd function


def lcm[T: (int, float)](a: T, b: T) -> T:
    return (a * b) // gcd(a, b)
