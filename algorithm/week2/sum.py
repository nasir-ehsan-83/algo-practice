def sum_of_nth_natural_number(n: int) -> int:
    total: int = 0
    for i in range(1, n + 1):
        total += i
    return total
