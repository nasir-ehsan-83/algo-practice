def eval_RPN(tokens: str) -> int:
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


def backspace_compare(s: str, t: str) -> bool:

    def process(string: str) -> str:
        stack: list[str] = []
        for c in string:
            if c == "#":
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

    return process(s) == process(t)


def remove_adjacent(s: str) -> str:
    stack: list[str] = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return "".join(stack)


type Char = str


def is_valid(s: str) -> bool:
    stack: list[Char] = []
    mapping: dict[Char, Char] = {")": "(", "]": "[", "}": "{"}

    for c in s:
        if c in "([{":
            stack.append(c)

        elif c in ")]}":
            if not stack or stack[-1] != mapping[c]:
                return False

            stack.pop()

    return not stack
