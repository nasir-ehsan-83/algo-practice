def evalRPN(tokens: str) -> int:
    stack: list[int] = []
    for token in tokens:
        if token in "+-*/":
            b: int = stack.pop()
            a: int = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # Integer division like LeetCode
        else:
            stack.append(int(token))

    return stack[0]
