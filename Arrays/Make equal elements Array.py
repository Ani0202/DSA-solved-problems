'''
Problem Description
 
 

Given an array of all positive integers and an element “x”. 

You need to find out whether all array elements can be made equal or not by performing any of the 3 operations: add x to any element in array, subtract x from any element from array, do nothing.

 This operation can be performed only once on an element of array.



Problem Constraints
1<=|A|<=1e5
1<=A[i],x<=1e9


Input Format
First argument is array of integers .
Second argument is B which denotes the value of x.


Output Format
Return 1 if we can make all elements equal , otherwise return 0.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if len(A) == 1:
            return 1

        nos = [A[0]-B, A[0], A[0]+B]
        for i in range(1, len(A)):
            if (A[i]-B in nos) or (A[i] in nos) or (A[i]+B in nos):
                continue
            else:
                return 0

        return 1