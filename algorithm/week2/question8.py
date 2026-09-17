def number_type(n: float | int) -> str:
    if n > 0: return "Positive";
    elif n < 0: return "Negative";
    else: return "Zero";
