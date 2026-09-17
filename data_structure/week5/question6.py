from question1 import Node;

class Queue[T]:
    front_node: Node[T] | None;
    rear_node: Node[T] | None;

    def __init__(self) -> None:
        self.front_node = None;
        self.rear_node = None;

    def isEmpty(self) -> bool:
        return self.front_node is None;

    def enqueue(self, data: T) -> None:
        new_node: Node[T] = Node(data);

        if self.rear_node:
            self.rear_node.next = new_node;
        
        self.rear_node = new_node;

        if not self.front_node:
            self.front_node = new_node;

    def dequeue(self) -> T | None:
        if self.isEmpty():
            return None;
    
        removed: T = self.front_node.data; # type: ignore
        self.front_node = self.front_node.next; # type: ignore

        if not self.front_node:
            self.rear_node = None;
        
        return removed;

    def front(self) -> T | None:
        if self.isEmpty():
            return None;
    
        return self.front_node.data; # type: ignore

    def rear(self) -> T | None:
        if self.isEmpty():
            return None;
    
        return self.rear_node.data;  # type: ignore

    def to_list(self) -> list[T]:
        result: list[T] = [];
        current: Node[T] | None = self.front_node;

        while current:
            result.append(current.data);
            current = current.next;
        
        return result;
