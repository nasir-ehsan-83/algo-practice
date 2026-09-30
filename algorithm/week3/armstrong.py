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
