class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, x: T) -> None:
        self.items.append(x)

    def pop(self) -> T | None:
        return self.items.pop() if self.items else None

    def peek(self) -> T | None:
        return self.items[-1] if self.items else None

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def top(self) -> T | None:
        if not self.items:
            return None

        return self.items[-1]

    def to_list(self) -> list[T]:
        return self.items.copy()

    def reverse(self) -> None:
        temp: list[T] = []
        while self.items:
            temp.append(self.items.pop())

        self.items = temp
