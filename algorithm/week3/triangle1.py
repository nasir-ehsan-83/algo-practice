def right_aligned_triangle(n: int) -> list[str]:
    pattern: list[str] = []

    for i in range(1, n + 1):
        pattern.append(" " * (n - i) + "*" * i)

    return pattern
