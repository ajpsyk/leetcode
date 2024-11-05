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
        return ListNode()

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


