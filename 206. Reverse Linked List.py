"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []
Constraints:

0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000

"""
from typing import Optional


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head is None case
        if head is None:
            return head

        # initalize a current and previous
        curr = head
        prev = None

        while curr is not None:
            # next is curr.next
            next = curr.next
            # curr.next is previous
            curr.next = prev
            # prev is curr
            prev = curr
            # curr is next
            curr = next

        return prev


solution = Solution()
head1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(3)
head1.next = node2
node2.next = node3
node3.next = node4

head2 = None


ll = solution.reverseList(head1)
while ll:
    print(ll.val)
    ll = ll.next
print(solution.reverseList(head2))











