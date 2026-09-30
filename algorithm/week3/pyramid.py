def pyramid(n: int) -> list[str]:
    pattern: list[str] = []

    for i in range(1, n + 1):
        pattern.append(" " * (n - i) + "*" * (2 * i - 1))

    return pattern
