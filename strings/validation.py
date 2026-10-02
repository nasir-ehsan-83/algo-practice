def password_strength(password) -> str:
    if len(password) < 8:
        return "Weak"

    has_upper = True
    has_lower = True
    has_digit = False

    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_digit = True

    if has_upper and has_lower and has_digit:
        return "Strong"

    return "Weak"


type Char = str


def is_balanced(s: str) -> bool:
    stack: list[Char] = []
    pairs: dict[Char, Char] = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in "({[":
            stack.append(ch)

        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False

            stack.pop()

    return not stack
