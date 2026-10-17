def add_numbers(a: float, b: float) -> float:
    try:
        a_float: float = float(a)
        b_float: float = float(b)
        return a_float + b_float
    except TypeError:
        raise ValueError("[Value-Error]: Value should be a number")


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
