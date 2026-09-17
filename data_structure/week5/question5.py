from question1 import Node;


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

    def search(self, data: T) -> bool:
        current: Node[T] | None = self.head;

        while current:
            if current.data == data:
                return True;
        
            current = current.next;
        
        return False;
