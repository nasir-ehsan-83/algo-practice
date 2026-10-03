def count_digits(n: int) -> int:
    count: int = 0

    while n > 0:
        count += 1
        n //= 10

    return count


def sum_of_digits(n: int) -> int:
    total: int = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def reverse_number(n: int) -> int:
    rev: int = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return rev
