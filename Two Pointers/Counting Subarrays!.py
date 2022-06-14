"""
Given an array A of N non-negative numbers and you are also given non-negative number B.

You need to find the number of subarrays in A having sum less than B. We may assume that there is no overflow.



Problem Constraints
1 <= N <= 104

1 <= A[i] <= 100

1 <= B <= 108



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the number of subarrays in A having sum less than B.
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        start = 0
        end = 0
        summ = A[0]
        count = 0
        while start < n and end < n:
            if summ < B:
                end += 1
                if start < end:
                    count += end - start
                if end < n:
                    summ += A[end]
            else:
                summ -= A[start]
                start += 1
        return count

