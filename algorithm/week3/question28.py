def remove_duplicates[T](arr: list[T]) -> list[T]:
    result: list[T] = [];
    seen: set[T] = set();

    for num in arr:
        if num not in seen:
            result.append(num);
            seen.add(num);
    
    return result;