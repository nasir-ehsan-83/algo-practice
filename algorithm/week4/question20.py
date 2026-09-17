type char = str;

def is_balanced(s: str) -> bool:
    stack: list[char] = [];
    pairs: dict[char, char] = {
        ')':'(', 
        '}':'{', 
        ']':'['
    };

    for ch in s:
        if ch in "({[":
            stack.append(ch);
        
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False;
        
            stack.pop();
    
    return not stack;
