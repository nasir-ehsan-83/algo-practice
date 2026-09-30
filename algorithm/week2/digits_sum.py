def sum_of_digits(n: int) -> int:
    total: int = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total
