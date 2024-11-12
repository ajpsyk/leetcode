"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # concat all linked lists
        # declare a length counter
        l = 0
        # for all lists in list
        for i in range(len(lists)):
            # iterate over list starting from head until next is None
            curr_node = lists[i]
            prev = None
            while curr_node:
                l += 1
                prev = curr_node
                curr_node = curr_node.next
                # increment length counter
            # if current index + 1 is not out of bounds
            if i + 1 <= len(lists) - 1:
                # set tail.next to head of next list
                prev.next = lists[i + 1]
        # perform merge sort on giant list, pass in starting index and length minus one
        return self.mergeKListsHelper(lists[0], 0, l - 1)

    # define a recursive helper function
    def mergeKListsHelper(self, list: List[Optional[ListNode]], s, e) -> Optional[ListNode]:
        if e - s + 1 <= 1:
            return list

        m = s + (e - s) // 2
        self.mergeKListsHelper(list, s, m)
        self.mergeKListsHelper(list, m + 1, e)
        self.merge(list, s, m, e)
        return list

    # define a merge function
    def merge(self, list, s, m, e):
        # find node at start and middle indices
        left = list
        curr_index = 0
        while curr_index < s:
            curr_index += 1
            left = left.next

        right = list
        curr_index = 0
        while curr_index < m + 1:
            curr_index += 1
            right = right.next

        curr = None
        if left.val <= right.val:
            curr = left
            left = left.next
        else:
            curr = right
            right = right.next

        while left and right:
            if left.val <= right.val:
                curr.next = left
                curr = left
                left = left.next
            else:
                curr.next = right
                curr = right
                right = right.next

        while left:
            curr.next = left
            curr = left
            left = left.next
        while right:
            curr.next = right
            curr = right
            right = right.next

solution = Solution()
lists = []
list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
lists.append(list1)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
lists.append(list2)
list3 = ListNode(2)
list3.next = ListNode(6)
lists.append(list3)
list = solution.mergeKLists(lists)
print()