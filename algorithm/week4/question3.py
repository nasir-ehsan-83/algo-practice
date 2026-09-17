def rotate_right[T](arr: list[T], k: float) -> list[T]:
    n = len(arr);

    if n == 0:
        return arr;

    k = k % n;
    return arr[-k:] + arr[:-k];
