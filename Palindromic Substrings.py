'''
Problem Description
 
 

Given a string A consisting of only lowercase English letters.
Return the number of substrings of A which are palindrome.


Problem Constraints
1 <= A <= 103


Input Format
The first and only argument is a string A.


Output Format
Return an integer.
'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        dp = [[0 for j in range(len(A))] for i in range(len(A))]
        ans = 0

        for i in range(len(A) - 1, -1, -1):
            for j in range(i, len(A)):
                if i == j:
                    ans += 1
                    dp[i][j] = 1
                elif A[i] == A[j]:
                    if j == i+1 or dp[i+1][j-1]:
                        ans += 1
                        dp[i][j] = 1

        return ans