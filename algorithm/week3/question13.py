def power(a: int | float, b: int) -> int | float:
    result: int | float = 1;

    for _ in range(b):
        result *= a;
    
    return result;
