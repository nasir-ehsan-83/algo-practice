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


class MinStack[T: (int, float)]:
    def __init__(self) -> None:
        self.stack: list[T] = []
        self.min_stack: list[T] = []

    def push(self, data: T) -> None:
        self.stack.append(data)
        if not self.min_stack or data <= self.min_stack[-1]:
            self.min_stack.append(data)

    def pop(self) -> T | None:
        if not self.stack:
            return None

        data: T = self.stack.pop()
        if data == self.min_stack[-1]:
            self.min_stack.pop()

        return data

    def top(self) -> T | None:
        if not self.stack:
            return None

        return self.stack[-1]

    def getMin(self) -> None | T:
        if not self.min_stack:
            return None

        return self.min_stack[-1]

    def to_list(self) -> list[T]:
        return self.stack.copy()
