'''
Problem Description

Given a set of N intervals denoted by 2D array A of size N x 2, the task is to find the length of maximal set of mutually disjoint intervals.

Two intervals [x, y] & [p, q] are said to be disjoint if they do not have any point in common.

Return a integer denoting the length of maximal set of mutually disjoint intervals.



Problem Constraints
1 <= N <= 105

1 <= A[i][0] <= A[i][1] <= 109



Input Format
First and only argument is a 2D array A of size N x 2 denoting the N intervals.



Output Format
Return a integer denoting the length of maximal set of mutually disjoint intervals.
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        A.sort(key = lambda x: x[1])
        r1 = A[0][1]
        ans = 1
     
        for i in range(1, len(A)):
            l1 = A[i][0]
            r2 = A[i][1]
            if l1 > r1:
                ans += 1
                r1 = r2

        return ans