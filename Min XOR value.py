'''
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer denoting minimum xor value
Constraints:

2 <= N <= 100 000  
0 <= A[i] <= 1 000 000 000
'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def findMinXor(self, A):
        A = sorted(A)
        n = len(A)
        ans = A[0]^A[1]
        for i in range(1, n-1):
            ans = min(ans, A[i]^A[i+1])

        return ans
