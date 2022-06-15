"""
Given a N * 2 array A where (A[i][0], A[i][1]) represents the ith pair.

In every pair, the first number is always smaller than the second number.

A pair (c, d) can follow another pair (a, b) if b < c , similarly in this way a chain of pairs can be formed.

Find the length of the longest chain subsequence which can be formed from a given set of pairs.



Problem Constraints
1 <= N <= 103

1 <= A[i][0] < A[i][1] <= 104



Input Format
First and only argument is an 2D integer array A of size N * 2 representing the N pairs.



Output Format
Return a single integer denoting the length of longest chain subsequence of pairs possible under given constraint.
"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if A[i][0] > A[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
