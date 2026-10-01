def add_numbers[T: (int, float)](a: T, b: T) -> T:
    return a + b


def simple_interest(p: float, r: float, t: int) -> float:
    return (p * r * t) // 100


def compound_interest(p: float, r: float, t: int) -> float:
    amount: float = p
    for _ in range(t):
        amount = amount + (amount * r // 100)

    return amount - p
