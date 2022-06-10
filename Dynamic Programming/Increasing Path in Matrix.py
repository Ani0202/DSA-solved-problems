'''
Given a 2D integer matrix A of size N x M.

 

 

From A[i][j] you can move to A[i+1][j], if A[i+1][j] > A[i][j], or can move to A[i][j+1] if A[i][j+1] > A[i][j].

The task is to find and output the longest path length possible if we start from the cell (0, 0) and want to reach cell (N - 1, M - 1).

NOTE:

 

 

If there doesn't exist a path return -1.


Problem Constraints
1 <= N, M <= 103

1 <= A[i][j] <= 108



Input Format
First and only argument is an 2D integer matrix A of size N x M.



Output Format
Return a single integer denoting the length of longest path in the matrix if no such path exists return -1.
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        M = len(A[0])

        dp = [[0 for i in range(M)] for j in range(N)]
        dp[0][0] = 1
        for i in range(1, N):
            if A[i][0] > A[i-1][0]:
                dp[i][0] = dp[i-1][0] + 1
            else:
                break

        for j in range(1, M):
            if A[0][j] > A[0][j-1]:
                dp[0][j] = dp[0][j-1] + 1
            else:
                break

        for i in range(1, N):
            for j in range(1, M):
                if A[i][j] > A[i-1][j] and dp[i-1][j] != 0:
                    u = dp[i-1][j] + 1
                else:
                    u = 0

                if A[i][j] > A[i][j-1] and dp[i][j-1] != 0:
                    l = dp[i][j-1] + 1
                else:
                    l = 0

                dp[i][j] = max(u, l)

        if dp[-1][-1]:
            return dp[-1][-1]

        else:
            return -1


