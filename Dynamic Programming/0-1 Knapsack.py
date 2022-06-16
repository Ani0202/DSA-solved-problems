"""
Given two integer arrays A and B of size N each which represent values and weights associated with N items respectively.

Also given an integer C which represents knapsack capacity.

Find out the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.

NOTE:

You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).


Problem Constraints
1 <= N <= 103

1 <= C <= 103

1 <= A[i], B[i] <= 103



Input Format
First argument is an integer array A of size N denoting the values on N items.

Second argument is an integer array B of size N denoting the weights on N items.

Third argument is an integer C denoting the knapsack capacity.



Output Format
Return a single integer denoting the maximum value subset of A such that sum of the weights of this subset is smaller than or equal to C.
"""


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(B)
        dp = [[0 for i in range(C + 1)] for j in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, C + 1):
                if B[i - 1] <= j:
                    dp[i][j] = max(A[i - 1] + dp[i - 1][j - B[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][C]
