def backspaceCompare(s: str, t: str) -> bool:

    def process(string: str) -> str:
        stack: list[str] = [];

        for c in string:
            if c == '#':
                if stack:
                    stack.pop();
            
            else:
                stack.append(c);
        
        return ''.join(stack);

    return process(s) == process(t);
