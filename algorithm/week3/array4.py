def count_occurrences[T](arr: list[T], x: T) -> int:
    count: int = 0;

    for num in arr:
        if num == x:
            count += 1;
    
    return count;