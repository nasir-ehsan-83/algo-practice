def multiplication_table(n: int, upto: int = 10) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []

    for i in range(1, upto + 1):
        result.append((n, i, n * i))

    return result
