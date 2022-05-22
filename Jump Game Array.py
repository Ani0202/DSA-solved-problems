'''
Given an array of non-negative integers, A, you are initially positioned at the 0th index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.



Input Format:

The first and the only argument of input will be an integer array A.
Output Format:

Return an integer, representing the answer as described in the problem statement.
    => 0 : If you cannot reach the last index.
    => 1 : If you can reach the last index.
Constraints:

    1 <= len(A) <= 106


    0 <= A[i] <= 30
'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def canJump(self, A):
        n = len(A)
        maxJump = 0
        for i in range(n):
            if i > maxJump:
                return 0
            maxJump = max(maxJump, i + A[i])

        return 1

