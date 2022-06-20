"""
Given an array A of size N denoting collection of numbers that might contain duplicates, return all possible unique permutations.

NOTE: No 2 entries in the permutation sequence should be the same.



Input Format
Only argument is an integer array A of size N.


Output Format
Return a 2-D array denoting all possible unique permutation of the array.
"""


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        n = len(A)
        A = sorted(A)
        temp = []
        ans = []
        self.findPerm(A, temp, ans, n)
        return ans

    def findPerm(self, A, temp, ans, n):
        if len(temp) == n:
            ans.append(list(temp))
            return

        for i in range(len(A)):
            if i != 0 and A[i] == A[i - 1]:
                continue
            temp.append(A[i])
            self.findPerm(A[:i] + A[i + 1:], temp, ans, n)
            temp.pop()
