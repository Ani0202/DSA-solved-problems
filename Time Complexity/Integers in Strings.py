"""
Given a string A, consisting of comma-separated positive integers.
Extract the given integers from the string and return an integer array consisting of the integers present in the string.

Note: All given integers will fit in a 32-bit signed integer.


Problem Constraints
1 <= |A| <= 105


Input Format
The first and only argument is a string A.


Output Format
Return an integer array.
The array should contain all the integers in the same order as they appear in the string.
"""


class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        res = []
        n = len(A)
        i = 0
        j = 0
        while j < n:
            if j == n - 1 or A[j + 1] == ',':
                res.append(int(A[i:j + 1]))
                i = j + 2
            j += 1

        return res
