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

        curr_node = head
        stack = []

        # traverse over list adding each element to stack
        # stop once last element is reached (its next element is None)
        while curr_node.next is not None:
            stack.append(curr_node)
            curr_node = curr_node.next


        # store current node as new head
        new_head = curr_node

        while len(stack) > 0:
            # pop from stack until empty
            # make current node's next the popped value
            curr_node.next = stack.pop()

            # advance current node to next
            curr_node = curr_node.next

        curr_node.next = None
        return new_head


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











