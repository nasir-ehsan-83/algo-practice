def kth_largest[T: (int, float, str)](arr: list[T], k: int) -> T:
    n: int = len(arr);

    for i in range(k):
        max_idx: int = i;
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j;
        
        arr[i], arr[max_idx] = arr[max_idx], arr[i];
    
    return arr[k-1];
