from question1 import Node;


class SinglyLinkedList[T]:
    head: Node[T] | None;

    def __init__(self) -> None:
        self.head = None;

    def append(self, data: T) -> None:
        """Add a node with value `data` at the end of the linked list."""

        new_node: Node[T] = Node(data);

        if not self.head:
            self.head = new_node;
            return;
    
        current: Node[T] | None = self.head;

        while current.next:
            current = current.next;
        
        current.next = new_node;

    def to_list(self) -> list[T]:
        """Convert linked list into a Python list."""

        result: list[T] = [];
        current: Node[T] | None = self.head;

        while current:
            result.append(current.data);
            current = current.next;
        
        return result;