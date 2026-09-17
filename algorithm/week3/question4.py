def factors(n: int) -> list[int]:
    result: list[int] = [];

    for i in range(1, n+1):
        if n % i == 0:
            result.append(i);
    
    return result;