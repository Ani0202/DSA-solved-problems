'''
Given a collection of numbers, return all possible permutations.

Example:

[1,2,3] will have the following permutations:

[1,2,3]
[1,3,2]
[2,1,3] 
[2,3,1] 
[3,1,2] 
[3,2,1]
NOTE

No two entries in the permutation sequence should be the same.
For the purpose of this problem, assume that all the numbers in the collection are unique.
Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.

Example : next_permutations in C++ / itertools.permutations in python.
'''

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
		ans = []
		temp = []
		self.findPer(ans, temp, A)
		return ans

	def findPer(self, ans, temp, A):
		if len(A) == 0:
			ans.append(list(temp))
			return

		for i in range(len(A)):
			temp.append(A[i])
			self.findPer(ans, temp, A[:i] + A[i+1:])
			temp.pop()


