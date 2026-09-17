class ATM:
    balance: float;

    def __init__(self) -> None:
        self.balance = 0;
    
    def deposit(self, amount: float) -> str:
        self.balance += amount;
        return f"{amount} deposited successfully";

    def withdraw(self, amount: float) -> str:
        if amount > self.balance:
            return "Insufficient balance";
    
        self.balance -= amount;
        return f"{amount} withdrawn successfully";

    def get_balance(self) -> float:
        return self.balance;
