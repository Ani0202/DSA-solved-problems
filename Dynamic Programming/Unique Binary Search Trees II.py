'''
Given an integer A, how many structurally unique BST’s (binary search trees) exist that can store values 1…A?

Input Format:

The first and the only argument of input contains the integer, A.
Output Format:

Return an integer, representing the answer asked in problem statement.
Constraints:

1 <= A <= 18
'''

class Solution:
    	# @param A : integer
	# @return an integer
	def numTrees(self, A):
        if A == 1:
            return 1
        if A == 2:
            return 2

        dp = [0 for i in range(A+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        for i in range(3, A+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]

        return dp[A]
