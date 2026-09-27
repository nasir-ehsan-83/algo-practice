# find maximum value between three valriables
def max_of_three[T: (int, float, str)](a: T, b: T, c: T) -> T:
    maximum: T = a
    maximum = max(maximum, b)
    maximum = max(maximum, c)
    return maximum
