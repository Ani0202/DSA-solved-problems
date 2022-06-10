'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
'''

class Solution:
    	# @param A : list of integers
	# @return a list of list of integers
	def subsetsWithDup(self, A):
        A = sorted(A)
        ans = [[]]
        temp = []
        self.findSubsets(ans, temp, 0, A)
        return ans

    def findSubsets(self, ans, temp, idx, A):
        for i in range(idx, len(A)):
            if i > idx and A[i] == A[i-1]:
                continue
            temp.append(A[i])
            ans.append(list(temp))
            self.findSubsets(ans, temp, i+1, A)
            temp.pop()

