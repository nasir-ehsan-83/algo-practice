# find maximum value between three valriables
def max_of_three[T: (int, float, str)](a: T, b: T, c: T) -> T:
    maximum: T = a;

    if b > maximum:
        maximum = b;
    
    if c > maximum:
        maximum = c;
    
    return maximum;
