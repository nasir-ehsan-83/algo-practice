class Node[T]:
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: Node | None = None
