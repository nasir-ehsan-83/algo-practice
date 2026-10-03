def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged: list[list[int]] = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]

        if current[0] <= last[1]:
            merged[-1] = [last[0], max(last[1], current[1])]

        else:
            merged.append(current)

    return merged


def intersection[T](arr1: list[T], arr2: list[T]) -> list[T]:
    result: list[T] = []

    for num in arr1:
        if num in arr2 and num not in result:
            result.append(num)

    return result
