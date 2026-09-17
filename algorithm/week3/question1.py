def count_vowels(s: str) -> int:
    vowels: str = "aeiouAEIOU";
    count: int = 0;

    for char in s:
        if char in vowels:
            count += 1;
    
    return count;