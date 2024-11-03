"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_paren = '({['
        closing_paren = ')}]'

        for i in range(len(s)):
            char = s[i]
            if char in opening_paren:
                stack.append(char)
            elif char in closing_paren:
                if len(stack) == 0:
                    return False
                peek = stack[len(stack) - 1]
                if closing_paren.index(char) != opening_paren.index(peek):
                    return False
                else:
                    stack.pop()

        if len(stack) != 0:
            return False

        return True

Solution = Solution()
print(Solution.isValid("[]"))
print(Solution.isValid("([{}])"))
print(Solution.isValid("[(])"))