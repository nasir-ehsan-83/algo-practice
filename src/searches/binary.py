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
