class QueueUsingStacks[T]:
    stack1: list[T];
    stack2: list[T];

    def __init__(self) -> None:
        self.stack1 = [];
        self.stack2 = [];

    def push(self, x) -> None:
        self.stack1.append(x);
    
    def pop(self) -> T | None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop());
        
        return self.stack2.pop() if self.stack2 else None
    
    def peek(self) -> T | None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop());
        
        return self.stack2[-1] if self.stack2 else None;

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2;
