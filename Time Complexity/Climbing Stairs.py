'''
Problem Description
 
 

Given an integer array A of length N. Where Ai is the cost of stepping on the ith stair.
From ith stair, you can go to i+1th or i+2th numbered stair.
Initially, you are at 1st stair find the minimum cost to reach Nth stair.


Problem Constraints
2 <= N <= 105
1 <= Ai <= 104


Input Format
The first and only argument is an integer array A.


Output Format
Return an integer.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 2:
            return A[0] + A[1]
        time = [0 for i in range(len(A))]
        time[0] = A[0]
        time[1] = A[0] + A[1]
        for i in range(2, len(A)):
            time[i] = min(time[i-1], time[i-2]) + A[i]

        return time[-1]
