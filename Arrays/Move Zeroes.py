'''
Problem Description
 
 

Given an integer array A, move all 0's to the end of it while maintaining the relative order of the non-zero elements.


Note that you must do this in-place without making a copy of the array.



Problem Constraints
1 <= |A| <= 105


Input Format
First argument is array of integers A.


Output Format
Return an array of integers which satisfies above property.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        i = 0
        j = 0
        while j < n:
            if A[j] != 0:
                A[j], A[i] = A[i], A[j]
                i += 1

            j += 1

        return A
