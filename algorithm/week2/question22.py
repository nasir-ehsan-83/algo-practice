def even_numbers(start: int, end: int) -> list[int]:
    result: list[int] = [];

    for i in range(start, end+1):
        if i % 2 == 0:
            result.append(i);
    
    return result;