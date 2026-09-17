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

    def reverse(self) -> None:
        temp: list[T] = [];

        while self.items:
            temp.append(self.items.pop());
        
        self.items = temp;

    def to_list(self) -> list[T]:
        return self.items.copy();
