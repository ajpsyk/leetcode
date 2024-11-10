"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
void addAtTail(int val) Append a node of value val as the last element of the linked list.
void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.


Example 1:

Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3


Constraints:

0 <= index, val <= 1000
Please do not use the built-in LinkedList library.
At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.
"""


class MyLinkedList:

    def __init__(self):
        # initialize a head that points to dummy node
        self.head = ListNode()
        # initialize a tail that points to the head initially
        self.tail = self.head

    def get(self, index: int) -> int:
        # declare a current index at zero
        curr_index = 0
        # declare current node to head
        curr_node = self.head.next
        # iterate over list until the end
        while curr_node:
            # if current index equals index
            if curr_index == index:
                # return value
                return curr_node.val
            curr_node = curr_node.next
            curr_index += 1

        return -1

    def addAtHead(self, val: int) -> None:

        # create a new list node
        new_node = ListNode(val)
        # set the next value to current head's next
        new_node.next = self.head.next
        new_node.prev = self.head
        # if head.next exists head.next.prev equals new node
        if self.head.next:
            self.head.next.prev = new_node
        # head.next equals new node
        self.head.next = new_node
        # if tail.next is not None
        if self.tail.next:
            # tail equals new node
            self.tail = new_node

    def addAtTail(self, val: int) -> None:

        # if head.next doesn't exist
        if self.head.next is None:
            # add value at head instead
            self.addAtHead(val)
        else:
            # create new list node
            new_node = ListNode(val)
            # tail.next equals new node
            self.tail.next = new_node
            # newnode.prev equals tail
            new_node.prev = self.tail
            # tail equals new node
            self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:

        # declare a flag
        found_node = None
        # current node is head.next
        curr_node = self.head.next
        # current index is zero
        curr_index = 0
        # iterate until current node is None
        while curr_node:
            # if current index equals index
            if curr_index == index:
                # set flag to current node
                found_node = curr_node
            # increment current index
            curr_index += 1
            # current node is current node's next
            curr_node = curr_node.next

        # if flag exists
        if found_node:
            # create new node
            new_node = ListNode(val)
            # new node next is current node
            new_node.next = found_node
            # new node prev is current node's prev
            new_node.prev = found_node.prev
            # current node's prev's next is new node
            found_node.prev.next = new_node
            # current node's prev is new node
            found_node.prev = new_node
        # if current index equals index
        if curr_index == index:
            # add value at tail
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        # declare a flag
        found_node = None
        # current node is head.next
        curr_node = self.head.next
        # current index is zero
        curr_index = 0
        # iterate until current node is None
        while curr_node:
            # if current index equals index
            if curr_index == index:
                # set flag to current node
                found_node = curr_node
            # increment current index
            curr_index += 1
            # current node is current node's next
            curr_node = curr_node.next

        # if flag exists
        if found_node:
            # flagged node's prev's next equals flagged node's next
            found_node.prev.next = found_node.next
            # flagged node's next's prev equals flagged node's prev
            if found_node.next:
                found_node.next.prev = found_node.prev
            else:
                self.tail = found_node.prev


# Create ListNode class, doubly linked node
# val, prev, next optional params
# defaults: 0, None, None
class ListNode:
    def __init__(self, val: int = 0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)