def pattern_match(pattern: str, s) -> bool:
    words: list[str] = s.split();

    if len(pattern) != len(words):
        return False;

    mapping: dict[str, str] = {};
    reverse_map: dict[str, str] = {};

    for p, w in zip(pattern, words):
        if p in mapping and mapping[p] != w:
            return False;
    
        if w in reverse_map and reverse_map[w] != p:
            return False;
    
        mapping[p] = w;
        reverse_map[w] = p;
    
    return True;