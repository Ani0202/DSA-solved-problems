'''
Given a sorted array, remove the duplicates in place such that each element can appear atmost twice and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

Note that even though we want you to return the new length, make sure to change the original array as well in place
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        k = 0
        i = 1
        for i in range(2,n):
            if A[i] == A[i-k-1] and A[i] == A[i-k-2]:
                if i >= 2 and A[i-2] == A[i]:
                    k += 1
            elif k > 0:
                A[i-k] = A[i]
        A = A[:n-k]
        return n-k
                