'''
Problem Description

Given an 1D integer array A containing N distinct integers.

Find the number of unique pairs of integers in the array whose XOR is equal to B.

NOTE:

Pair (a, b) and (b, a) is considered to be same and should be counted once.


Problem Constraints
1 <= N <= 105

1 <= A[i], B <= 107



Input Format
First argument is an 1D integer array A.

Second argument is an integer B.



Output Format
Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        count = dict()
        ans = 0
        for i in A:
            count[i] = count.get(i, 0) + 1
            ans += count.get(B^i, 0)

        return ans
