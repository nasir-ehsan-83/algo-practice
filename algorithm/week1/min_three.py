# find minimum value between three vrariables
def min_of_three[T: (int, float, str)](a: T, b: T, c: T) -> T:
    minimum: T = a
    minimum = min(minimum, b)
    minimum = min(minimum, c)
    return minimum
