def largest_smallest[T: (int, float)](a: T, b: T, c: T) -> tuple[T, T]:
    largest: T = a;
    if b > largest: largest = b;
    if c > largest: largest = c;

    smallest: T = a;
    if b < smallest: smallest = b;
    if c < smallest: smallest = c;

    return largest, smallest;