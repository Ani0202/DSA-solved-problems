'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        temp = []
        A = sorted(A)
        ans = []
        self.findComb(temp, ans, A, B, 0)
        return ans

    def findComb(self, temp, ans, A, B, idx):
        s = sum(temp)
        if s == B:
            ans.append(list(temp))
            return
        elif s > B:
            return

        for i in range(idx, len(A)):
            if i != idx and A[i] == A[i-1]:
                continue
            temp.append(A[i])
            self.findComb(temp, ans, A, B, i+1)
            temp.pop()

