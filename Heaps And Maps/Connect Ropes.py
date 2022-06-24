"""
Given an array of integers A representing the length of ropes.

You need to connect these ropes into one rope. The cost of connecting two ropes is equal to the sum of their lengths.

Find and return the minimum cost to connect these ropes into one rope.



Problem Constraints
1 <= length of the array <= 100000

1 <= A[i] <= 1000



Input Format
The only argument given is the integer array A.



Output Format
Return an integer denoting the minimum cost to connect these ropes into one rope.
"""
import heapq

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        heapq.heapify(A)
        ans = 0
        while len(A) > 1:
            n = heapq.heappop(A)
            m = heapq.heappop(A)
            a = n + m
            ans += a
            heapq.heappush(A, a)

        return ans
