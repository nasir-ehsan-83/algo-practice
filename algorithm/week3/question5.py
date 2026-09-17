def largest[T: (int, float)](arr: list[T]) -> T | None:
    if not arr:
        return None;
    
    max_val: T = arr[0];

    for num in arr:
        if num > max_val:
            max_val = num;
    
    return max_val;
