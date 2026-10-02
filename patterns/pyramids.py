def pyramid(n: int) -> list[str]:
    pattern: list[str] = []

    for i in range(1, n + 1):
        pattern.append(" " * (n - i) + "*" * (2 * i - 1))

    return pattern


def right_triangle(n: int) -> list[str]:
    pattern: list[str] = []

    for i in range(1, n + 1):
        pattern.append("*" * i)

    return pattern


def right_aligned_triangle(n: int) -> list[str]:
    pattern: list[str] = []

    for i in range(1, n + 1):
        pattern.append(" " * (n - i) + "*" * i)

    return pattern


def pascal_triangle(rows: int) -> list[list[int]]:
    result: list[list[int]] = []

    for i in range(rows):
        row: list[int] = [1] * (i + 1)

        for j in range(1, i):
            row[j] = result[i - 1][j - 1] + result[i - 1][j]

        result.append(row)

    return result


def multiplication_table(n: int, upto: int = 10) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []

    for i in range(1, upto + 1):
        result.append((n, i, n * i))

    return result
