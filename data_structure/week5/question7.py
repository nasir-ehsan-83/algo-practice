class Stack[T]:
    items: list[T];

    def __init__(self) -> None:
        self.items = [];

    def push(self, data: T) -> None:
        self.items.append(data);

    def pop(self) -> T | None:
        if not self.items:
            return None;
    
        return self.items.pop();

    def top(self) -> T | None:
        if not self.items:
            return None;
    
        return self.items[-1];

    def isEmpty(self) -> bool:
        return len(self.items) == 0;

    def size(self) -> int:
        return len(self.items);

    def to_list(self) -> list[T]:
        return self.items.copy();
