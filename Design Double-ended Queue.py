"""
Design a Double-ended Queue class.

Your Deque class should support the following operations:

Deque() will initialize an empty queue.
bool isEmpty() will return whether the queue is empty or not.
void append(int value) will insert value at the end of the queue.
void appendleft(int val) will insert value at the beginning of the queue.
int pop() will remove and return the value at the end of the queue. If the queue is empty, return -1.
int popleft() will remove and return the value at the beginning of the queue. If the queue is empty, return -1.
Note: You should implement each operation in
O
(
1
)
O(1) time complexity.

Example 1:

Input:
["isEmpty", "append", 10, "isEmpty", "appendLeft", 20, "popLeft", "pop", "pop", "append", 30, "pop", "isEmpty"]

Output:
[true, null, false, null, 20, 10, -1, null, 30, true]
"""

class Deque:

    def __init__(self):
        # create dummy node for tail and head
        self.head = DequeNode()
        self.tail= DequeNode()
        # set next and prev values
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        # if head.next is tail
        if self.head.next == self.tail:
            # return True
            return True
        # return False
        return False

    def append(self, value: int) -> None:
        # add at Tail
        # if list is empty, append left instead
        if self.isEmpty():
            self.appendleft(value)
        # otherwise create new node
        else:
            new_node = DequeNode(value)
            # new node.next = tail
            new_node.next = self.tail
            # new node.prev = tail.prev
            new_node.prev = self.tail.prev
            # tail.prev.next = new_node
            self.tail.prev.next = new_node
            # tail.prev = new_node
            self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        # add at Head
        # create new node
        new_node = DequeNode(value)
        # new node next equals head.next
        new_node.next = self.head.next
        # new node prev equals head
        new_node.prev = self.head
        # head.next.prev equals new node
        self.head.next.prev = new_node
        # head.next = new node
        self.head.next = new_node

    def pop(self) -> int:
        # remove at tail
        # removed node is tail.prev
        if self.isEmpty():
            return -1
        removed_node = self.tail.prev
        # removed node prev next equals tail
        removed_node.prev.next = self.tail
        # tail. prev equals removed_node's prev
        self.tail.prev = removed_node.prev
        # return removed node's value
        return removed_node.value

    def popleft(self) -> int:
        # remove at head
        # removed node is head.next
        if self.isEmpty():
            return -1
        removed_node = self.head.next
        # removed node's next.prev equals head
        removed_node.next.prev = self.head
        # head's next equals removed node's next
        self.head.next = removed_node.next
        # return removed node's value
        return removed_node.value
# create node class with val, prev and next data
class DequeNode:
    def __init__(self, value: int = 0):
        self.value = value
        self.prev = None
        self.next = None

