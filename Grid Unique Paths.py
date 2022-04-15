'''
A robot is located at the top-left corner of an A x B grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Note: A and B will be such that the resulting answer fits in a 32 bit signed integer.
'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def uniquePaths(self, A, B):
        a = A-1
        b = B-1
        if a == 0 or b == 0:
            return 1
        ans = 1
        if b > a:
            a, b = b, a

        for i in range(a+1, a+b+1):
            ans *= i

        for i in range(1, b+1):
            ans //= i
            
        return ans
