def number_type(n: float) -> str:
    if n > 0:
        return "Positive"

    elif n < 0:
        return "Negative"

    else:
        return "Zero"


def is_armstrong(n: int) -> bool:
    digits: list[int] = []
    temp: int = n

    while temp > 0:
        digits.append(temp % 10)
        temp //= 10

    power: int = len(digits)
    sum = 0

    for d in digits:
        sum += d**power

    return sum == n


def is_palindrome(n: int) -> bool:
    original: int = n
    rev: int = 0

    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10

    return rev == original


def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def factors(n: int) -> list[int]:
    result: list[int] = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result


def factorial(n: int) -> int:
    result: int = 1

    for i in range(1, n + 1):
        result *= i

    return result


def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)
