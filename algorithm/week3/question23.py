def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1;

    return n * factorial_recursive(n - 1);
