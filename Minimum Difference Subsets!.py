'''
Problem Description

Given an integer array A containing N integers.

You need to divide the array A into two subsets S1 and S2 such that the absolute difference between their sums is minimum.

Find and return this minimum possible absolute difference.

NOTE:

Subsets can contain elements from A in any order (not necessary to be contiguous).
Each element of A should belong to any one subset S1 or S2, not both.
It may be possible that one subset remains empty.


Problem Constraints
1 <= N <= 100

1 <= A[i] <= 100



Input Format
First and only argument is an integer array A.



Output Format
Return an integer denoting the minimum possible difference among the sums of two subsets.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        tot = sum(A)
        dp = [[0 for i in range(tot//2 + 1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, tot//2 + 1):
                if A[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - A[i-1]]

        for i in range(tot//2, -1, -1):
            if dp[n][i] == 1:
                return tot - 2*i
