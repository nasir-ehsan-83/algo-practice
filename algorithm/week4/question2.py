def merge_sorted_arrays[T: (int, float, str)](arr1: list[T], arr2: list[T]) -> list[T]:
    result: list[T] = [];
    i: int = 0;
    j: int = 0;
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i]);
            i += 1;
        
        else:
            result.append(arr2[j]);
            j += 1;
    
    while i < len(arr1):
        result.append(arr1[i]);
        i += 1;
    
    while j < len(arr2):
        result.append(arr2[j]);
        j += 1;
    
    return result;