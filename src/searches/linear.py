def linear_search[T: (int, float, str)](list: list[T], target: T) -> int | None:
    for i in range(len(list)):
        if list[i] == target:
            return i

    return None
