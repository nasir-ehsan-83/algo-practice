def largest_smallest[T: (int, float)](a: T, b: T, c: T) -> tuple[T, T]:
    largest: T = a
    largest = max(largest, b)
    largest = max(largest, c)
    smallest: T = a
    smallest = min(smallest, b)
    smallest = min(smallest, c)
    return largest, smallest
