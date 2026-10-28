def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def primes_up_to(n: int) -> list[int]:
    result: list[int] = []

    for num in range(2, n + 1):
        prime: bool = True

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break

        if prime:
            result.append(num)

    return result


def decimal_to_binary(n: int) -> str:
    if n == 0:
        return "0b0"

    if n < 0:
        return "-" + decimal_to_binary(-n)

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return "0b" + binary
