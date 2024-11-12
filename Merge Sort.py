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
    # Implementation of Merge Sort
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs

        # The middle index of the array
        m = (s + e) // 2

        # Sort the left half
        self.mergeSortHelper(pairs, s, m)

        # Sort the right half
        self.mergeSortHelper(pairs, m + 1, e)

        # Merge sorted halfs
        self.merge(pairs, s, m, e)

        return pairs

    # Merge in-place
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        # Copy the sorted left & right halfs to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0  # index for L
        j = 0  # index for R
        k = s  # index for arr

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halfs will have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

solution = Solution()
solution.mergeSort([(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")])
