def find_missing_number[T: (int, float)](arr: list[T], N: T) -> T:
    total = N * (N + 1) // 2;
    sum_arr = 0;

    for num in arr:
        sum_arr += num;
    
    return total - sum_arr;