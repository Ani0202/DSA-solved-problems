'''
Given a 2D binary matrix A of size  N x M  find the area of maximum size square sub-matrix with all 1's.



Problem Constraints
1 <= N, M <= 103

 A[i][j] = 1 or A[i][j] = 0



Input Format
First argument is an 2D matrix A of size N x M.



Output Format
Output the area of maximum size square sub-matrix in A with all 1's.
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        M = len(A[0])

        ans = 0
        for i in range(N):
            for j in range(M):
                if i == 0 or j == 0:
                    ans = max(ans, A[i][j])
                    continue
                elif A[i][j] == 1:
                    l = min(A[i-1][j], A[i][j-1], A[i-1][j-1])
                    if l == 0:
                        ans = max(ans, A[i][j])
                    else:
                        A[i][j] = l + 1
                        ans = max(ans, A[i][j])

        return ans*ans
