'''
Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
'''

class Solution:
	# @param A : integer
	# @param B : integer
	# @return a list of list of integers
	def combine(self, A, B):
        ans = []

        def findComb(temp, idx):
            if len(temp) == B:
                ans.append(list(temp))
                return

            if len(temp) > B:
                return

            for i in range(idx, A+1):
                temp.append(i)
                findComb(temp, i+1)
                temp.pop()

        findComb([], 1)
        return ans
