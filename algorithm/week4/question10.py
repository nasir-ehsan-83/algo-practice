def is_unique[T](s: list[T]) -> bool:
    seen: set[T] = set();
    
    for ch in s:
        if ch in seen:
            return False;
    
        seen.add(ch);
    
    return True;