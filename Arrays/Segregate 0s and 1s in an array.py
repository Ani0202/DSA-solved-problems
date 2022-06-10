'''
Problem Description
 
 


You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the 
array]. Traverse array only once. 



Problem Constraints
1<=|A|<=1e6


Input Format
First argument is array of integers consisting of 0's and 1's only.


Output Format
Return a sorted array.
'''

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        i = 0
        j = 0
        while j < len(A):
            if A[j] == 0:
                A[i], A[j] = A[j], A[i]
                i += 1

            j += 1

        return A
