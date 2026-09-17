def factorial(n: int) -> int:
    result: int = 1;

    for i in range(1,n+1):
        result *= i;
    
    return result;
