def second_largest(arr: list[float]) -> float | None:
    if len(arr) < 2:
        return None;

    first: float = float("-inf");
    second: float = float('-inf');

    for num in arr:
        if num > first:
            second = first;
            first = num;
        
        elif num > second and num != first:
            second = num;
    
    return second;