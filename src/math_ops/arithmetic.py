def add_numbers[T: (int, float)](a: T, b: T) -> T:
    return a + b


def simple_interest(p: float, r: float, t: int) -> float:
    return (p * r * t) // 100


def compound_interest(p: float, r: float, t: int) -> float:
    amount: float = p
    for _ in range(t):
        amount = amount + (amount * r // 100)

    return amount - p


def power(a: float, b: int) -> int | float:
    result: int | float = 1

    for _ in range(b):
        result *= a

    return result


def swap[T](a: T, b: T) -> tuple[T, T]:
    return b, a
