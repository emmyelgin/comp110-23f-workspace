"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Return data of first element in list."""
        return self.data
    
    def tail(self) -> Node | None:
        """Return list of every element minus the head."""
        return self.next 
    
    def last(self) -> int:
        """Return data of the last element on list."""
        if self.next is None:
            return self.data
        else:
            return self.next.last()

        
node_c: Node = Node(2, None) 
node_b: Node = Node(1, node_c)
node_a: Node = Node(0, node_b) 

print("Actual: ", node_a.head(), " - Expected: 0")

print("Actual: ", node_a.tail(), " - Expected: 1 -> 2 -> None")
print("Actual: ", node_c.tail(), " - Expected: None")

print("Actual: ", node_a.last(), " - Expected: 2")