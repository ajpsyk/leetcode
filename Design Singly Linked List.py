"""
Design a Singly Linked List class.

Your LinkedList class should support the following operations:

LinkedList() will initialize an empty linked list.
int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
void insertHead(int val) will insert a node with val at the head of the list.
void insertTail(int val) will insert a node with val at the tail of the list.
bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
Example 1:

Input:
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
Note:

The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.
"""

from typing import List


class LinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr_node = self.head
        curr_index = 0

        while curr_node is not None:
            if curr_index == index:
                return curr_node.val
            curr_index += 1
            curr_node = curr_node.next

        return -1




    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
        else:
            new_node = ListNode(val)
            new_node.next = self.head
            self.head = new_node

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
        else:
            curr_node = self.head

            while curr_node.next is not None:
                curr_node = curr_node.next

            curr_node.next = ListNode(val)

    def remove(self, index: int) -> bool:
        # list is empty
        if self.head is None:
            return False
        # index to remove is head
        if index == 0:
            self.head = self.head.next
            return True

        # index to remove is not head and is a valid index
        # index to remove is out of bounds
        curr_node = self.head
        next_index = 1

        while curr_node.next is not None:
            if next_index == index:
                curr_node.next = curr_node.next.next
                return True
            next_index += 1
            curr_node = curr_node.next

        return False

    def getValues(self) -> List[int]:
        values = []
        curr_node = self.head

        while curr_node is not None:
            values.append(curr_node.val)
            curr_node = curr_node.next

        return values

class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.next = None

ll = LinkedList()
ll.insertTail(1)
ll.insertTail(2)
print(ll.get(1))

ll = LinkedList()
ll.insertHead(1)
ll.insertTail(2)
ll.insertHead(0)
print(ll.remove(1)) # true
print(ll.getValues()) # [0,2]

ll = LinkedList()
ll.insertHead(1)
ll.insertHead(2)
print(ll.get(5)) # -1