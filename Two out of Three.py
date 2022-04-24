'''
Problem Description

Given are Three arrays A, B and C.

Return the sorted list of numbers that are present in atleast 2 out of the 3 arrays.



Problem Constraints
1 <= |A|, |B|, |C| <= 100000

1 <= A[i], B[i], C[i] <= 100000

A, B, C may or may not have pairwise distinct elements.



Input Format
First argument is the array A.

First argument is the array B.

First argument is the array C.



Output Format
Return a sorted array of numbers.
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        count = dict()
        for i in set(A):
            count[i] = 1

        for i in set(B):
            count[i] = count.get(i, 0) + 1

        for i in set(C):
            count[i] = count.get(i, 0) + 1

        ans = []
        for k in count.keys():
            if count[k] > 1:
                ans.append(k)

        return sorted(ans)
