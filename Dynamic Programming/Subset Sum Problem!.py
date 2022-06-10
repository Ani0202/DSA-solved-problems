'''
Given an integer array A  of size N.

You are also given an integer B, you need to find whether their exist a subset in A whose sum equal B.

If there exist a subset then return 1 else return 0.



Problem Constraints
1 <= N <= 100

1 <= A[i] <= 100

1 <= B <= 105



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return 1 if there exist a subset with sum B else return 0.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        dp = [[0 for i in range(B+1)] for j in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n+1):
            for j in range(1, B+1):
                if A[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - A[i-1]]

        return dp[n][B]