def contains[T](arr: list[T], x: T) -> bool:
    for num in arr:
        if num == x:
            return True

    return False
