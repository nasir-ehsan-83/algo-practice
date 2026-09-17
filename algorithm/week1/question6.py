# find minimum value between three vrariables
def min_of_three[T: (int, float, str)](a: T, b: T, c: T) -> T:
    minimum: T = a;

    if b < minimum:
        minimum = b;
    
    if c < minimum:
        minimum = c;
    
    return minimum;
