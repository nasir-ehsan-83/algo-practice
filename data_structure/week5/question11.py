class QueueTwoStacks[T]:
    stack_in: list[T];
    stack_out: list[T];

    def __init__(self) -> None:
        self.stack_in = [];
        self.stack_out = [];

    def push(self, data: T) -> None:
        self.stack_in.append(data);

    def pop(self) -> T | None:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop());
        
        if not self.stack_out:
            return None;
    
        return self.stack_out.pop();

    def peek(self) -> T | None:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop());
        
        if not self.stack_out:
            return None;
    
        return self.stack_out[-1];

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out;
