"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:



Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]
Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]
Example 3:

Input: list1 = [], list2 = []

Output: []
Constraints:

0 <= The length of the each list <= 100.
-100 <= Node.val <= 100
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # empty list cases
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # initalize head to lowest of both heads, prioritize list1 if equal
        # initialze pointer to next value of lower head
        # initialize pointer to higher head
        if list2.val < list1.val:
            head = list2
            curr1 = list1
            curr2 = list2.next
        else:
            head = list1
            curr1 = list1.next
            curr2 = list2


        # initialize current to head
        curr = head
         # repeat until both pointers are null
        while curr1 is not None or curr2 is not None:
            # compare pointer values
            # current.next equals lower or non null pointer
            # lower pointer equals lower pointer's next
            # current equals current's next
            if curr1 is None or (curr2 is not None and curr2.val < curr1.val):
                curr.next = curr2
                curr2 = curr2.next
            elif curr2 is None or (curr1 is not None and curr1.val <= curr2.val):
                curr.next = curr1
                curr1 = curr1.next

            curr = curr.next



        return head

solution = Solution()
list1node1 = ListNode(1)
list1node2 = ListNode(2)
list1node3 = ListNode(4)
list1node1.next = list1node2
list1node2.next = list1node3

list2node1 = ListNode(1)
list2node2 = ListNode(3)
list2node3 = ListNode(5)
list2node1.next = list2node2
list2node2.next = list2node3

ll = solution.mergeTwoLists(list1node1, list2node1)
while ll:
    print(ll.val)
    ll = ll.next

list1 = None
list2 = ListNode(1)
list2.next = ListNode(2)
ll = solution.mergeTwoLists(list1, list2)
while ll:
    print(ll.val)
    ll = ll.next


