"""
Implement Merge Sort.

Merge Sort is a divide-and-conquer algorithm for sorting an array or list of elements. It works by recursively dividing the unsorted list into n sub-lists, each containing one element. Then, it repeatedly merges sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.

Objective:

Given a list of key-value pairs, sort the list by key using Merge Sort. If two key-value pairs have the same key, maintain their relative order in the sorted list.

Input:

pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).
Example 1:

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]

Output:
[(1, "date"), (2, "banana"), (5, "apple"), (9, "cherry"), (9, "elderberry")]
Note: As you can see, the solution is always stable. The two pairs with the key 9 maintained their relative positions.

Example 2:

Input:
pairs = [(3, "cat"), (2, "dog"), (3, "bird")]

Output:
[(2, "dog"), (3, "cat"), (3, "bird")]
"""
from typing import List
# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair], start=-1, end=-1) -> List[Pair]:

        # calculate start and end index if initial call
        if start == -1:
            start = 0
            end = len(pairs) - 1

        # case: list is 1 element or less
        if end - start <= 1:
            return pairs
        # case: list is greater than 1 element
        # calculate middle index
        middle = (end - start) // 2
        # recursivley call left
        left = self.mergeSort(pairs, start, middle)
        # recursivley call right
        right = self.mergeSort(pairs, middle + 1, end)
        # merge left and right
        # create new list
        new_list = []
        # pointer to first element of array
        curr_new_index = 0
        # set a pointer to start of left and right
        curr_left_index = start
        curr_right_index = middle + 1
        # while left and right pointer are at valid indices
        while curr_left_index <= middle and curr_right_index <= end:
            # if element at left pointer is less than or equal to right pointer
            if pairs[curr_left_index].key <= pairs[curr_right_index].key:
                # append left pointer element to new list
                new_list.append(pairs[curr_left_index])
                # advance left pointer
                curr_left_index += 1
            # else
            else:
                # append right pointer element to new list
                new_list.append(pairs[curr_left_index])
                # advance right pointer
                curr_right_index += 1
            curr_new_index += 1
        # return new list
        return new_list

solution = Solution()
solution.mergeSort([(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")])
