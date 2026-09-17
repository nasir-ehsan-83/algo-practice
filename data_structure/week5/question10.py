class MinStack[T: (int, float)]:
    stack: list[T];
    min_stack: list[T];

    def __init__(self) -> None:
        self.stack = [];
        self.min_stack = [];

    def push(self, data: T) -> None:
        self.stack.append(data);
        
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self) -> T | None:
        if not self.stack:
            return None;
    
        data: T = self.stack.pop();

        if data == self.min_stack[-1]:
            self.min_stack.pop();
        
        return data;

    def top(self) -> T | None:
        if not self.stack:
            return None;
    
        return self.stack[-1];

    def getMin(self) -> None | T:
        if not self.min_stack:
            return None;
    
        return self.min_stack[-1];

    def to_list(self) -> list[T]:
        return self.stack.copy();
