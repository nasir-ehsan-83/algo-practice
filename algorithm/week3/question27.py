def unique_elements[T](arr: list[T]) -> list[T]:
    result: list[T] = [];

    for num in arr:
        if num not in result:
            result.append(num);
    
    return result;