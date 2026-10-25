def count_digits(n: int) -> int:
    count: int = 0
    is_negative: bool = False

    if n < 0:
        is_negative = True

    n = abs(n)
    while n > 0:
        count += 1
        n //= 10

    if is_negative:
        return -1 * count

    return count


def sum_of_digits(n: int) -> int:
    total: int = 0
    n = abs(n)

    while n > 0:
        total += n % 10
        n //= 10

    return total


def reverse_number(n: int) -> int:
    rev: int = 0
    is_negative: bool = False

    if n < 0:
        is_negative = True

    n = abs(n)

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    if is_negative:
        return -1 * rev

    return rev
