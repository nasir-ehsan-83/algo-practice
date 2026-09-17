class Node[T]:
    data: T;
    next: Node[T] | None;

    def __init__(self, data) -> None:
        self.data = data;
        self.next = None;


class SinglyLinkedList[T]:
    head: Node[T] | None;

    def __init__(self) -> None:
        self.head = None;

    def append(self, data: T) -> None:
        new_node: Node[T] = Node(data);

        if not self.head:
            self.head = new_node;
            return;
    
        current: Node[T] | None = self.head;

        while current.next:
            current = current.next;
        
        current.next = new_node;

    def to_list(self) -> list[T]:
        result: list[T] = [];
        current: Node[T] | None = self.head;

        while current:
            result.append(current.data);
            current = current.next;
        
        return result;