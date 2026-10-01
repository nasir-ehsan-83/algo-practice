def intersection[T](arr1: list[T], arr2: list[T]) -> list[T]:
    result: list[T] = []

    for num in arr1:
        if num in arr2 and num not in result:
            result.append(num)

    return result
