type char = str;

def isValid(s: str) -> bool:
    stack: list[char] = [];
    mapping: dict[char, char] = {
        ')':'(', 
        ']':'[', 
        '}':'{'
    };

    for c in s:
        if c in "([{":
            stack.append(c);
        
        elif c in ")]}":
            if not stack or stack[-1] != mapping[c]:
                return False;
        
            stack.pop();
    
    return not stack;