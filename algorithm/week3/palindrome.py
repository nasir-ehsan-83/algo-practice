def is_palindrome(n: int) -> bool:
    original: int = n
    rev: int = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return rev == original
