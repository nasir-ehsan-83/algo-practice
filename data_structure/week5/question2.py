from question1 import (
    SinglyLinkedList, 
    Node
);

class SinglyLinkedListWithInsert[T](SinglyLinkedList):
    head: Node[T] | None;

    def insert_at_beginning(self, data: T) -> None:
        new_node: Node[T] = Node(data);
        new_node.next = self.head;
        self.head = new_node;