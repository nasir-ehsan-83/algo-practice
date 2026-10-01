def calculator[T: (int, float)](a: T, b: T, op: str) -> T | None:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a // b if b != 0 else None
    else:
        return None
