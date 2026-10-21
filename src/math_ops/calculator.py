def calculator[T: (int, float)](first: T, second: T, op: str) -> T | None:
    match op:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            return first // second if second != 0 else None
        case "%":
            return first % second if second != 0 else None

    return None
