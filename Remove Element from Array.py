'''
Remove Element

Given an array and a value, remove all the instances of that value in the array. 

Also return the number of elements left in the array after the operation.

It does not matter what is left beyond the expected length.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        ans = 0
        i = 0
        j = 0
        while j < len(A):
            if A[j] != B:
                A[i], A[j] = A[j], A[i]
                ans += 1
                i += 1

            j += 1
            
        return ans
