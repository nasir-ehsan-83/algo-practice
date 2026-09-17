class Stack[T]:
    items: list[T];

    def __init__(self) -> None:
        self.items = [];
    
    def push(self, x: T) -> None:
        self.items.append(x);
    
    def pop(self) -> T | None:
        return self.items.pop() if self.items else None;

    def peek(self) -> T | None:
        return self.items[-1] if self.items else None;

    def is_empty(self) -> bool:
        return len(self.items) == 0;

    def size(self) -> int:
        return len(self.items);