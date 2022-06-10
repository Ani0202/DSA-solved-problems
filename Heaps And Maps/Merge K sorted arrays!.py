'''
Problem Description

You are given K sorted integer arrays in a form of 2D integer matrix A of size K X N.

You need to merge them into a single array and return it.



Problem Constraints
1 <= K, N <= 103

0 <= A[i][j] <= 108

A[i][j] <= A[i][j+1]



Input Format
First and only argument is an 2D integer matrix A.



Output Format
Return a integer array denoting the merged array you get after merging all the arrays in A.
'''

import heapq

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        heap = []
        K = len(A)
        N = len(A[0])
        for i in range(K):
            heapq.heappush(heap, (A[i][0], i, 0))

        ans = []
        while len(heap):
            a, b, c = heapq.heappop(heap)
            ans.append(a)
            if c+1 < N:
                heapq.heappush(heap, (A[b][c+1], b, c+1))

        return ans
