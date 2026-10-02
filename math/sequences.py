def fibonacci(n: int) -> list[int]:
    if n <= 0:
        return []

    series: list[int] = [0]
    if n == 1:
        return series

    series.append(1)
    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])

    return series


def collatz_sequence(n: int) -> tuple[list[int], int]:
    seq: list[int] = [n]
    steps: int = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        seq.append(n)
        steps += 1

    return seq, steps


def sum_of_nth_natural_number(n: int) -> int:
    total: int = 0
    for i in range(1, n + 1):
        total += i
    return total


def even_numbers(start: int, end: int) -> list[int]:
    result: list[int] = []

    for i in range(start, end + 1):
        if i % 2 == 0:
            result.append(i)

    return result


def list_of_nth_numbers(n: int) -> list[int]:
    result: list[int] = []

    for i in range(n):
        result.append(i)

    return result
