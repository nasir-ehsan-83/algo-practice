# compute simple interest
def simple_interest(p: float, r: float, t: int) -> float:
    return (p * r * t) // 100;

# compute compound interest
def compound_interest(p: float, r: float, t: int) -> float:
    amount: float = p;

    for _ in range(t):
        amount = amount + (amount * r // 100);
    
    return amount - p;
