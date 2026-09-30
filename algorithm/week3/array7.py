def arrays_equal[T](arr1: list[T], arr2: list[T]) -> bool:
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True
