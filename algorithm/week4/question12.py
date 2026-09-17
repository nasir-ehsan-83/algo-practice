def char_frequency(s: str) -> dict[str, int]:
    freq: dict[str, int] = {};

    for ch in s:
        if ch in freq:
            freq[ch] += 1;
        
        else:
            freq[ch] = 1;
    
    return freq;
