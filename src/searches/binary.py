def binary_search[T: (int, float, str)](arr: list[T], target: T) -> int:
    left: int = 0
    right: int = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1


def binary_search_recursive[T: (int, float, str)](list: list[T], target: T) -> int:
    if len(list) == 0:
        return -1

    else:
        mid: int = len(list) // 2

        if list[mid] == target:
            return mid
        else:
            if list[mid] < target:
                return binary_search_recursive(list[mid + 1 :], target)
            else:
                return binary_search_recursive(list[:mid], target)
