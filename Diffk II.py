'''
Given an array A of integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
'''

class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
        hmap = dict()
        n = len(A)
        for i in range(n):
            if B + A[i] in hmap or A[i] - B in hmap:
                return 1
            hmap[A[i]] = 1

        return 0
