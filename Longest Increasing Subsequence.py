'''
Find the longest increasing subsequence of a given array of integers, A.

In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, and in which the subsequence is as long as possible. 

This subsequence is not necessarily contiguous, or unique.

In this case, we only care about the length of the longest increasing subsequence.



Input Format:

The first and the only argument is an integer array A.
Output Format:

Return an integer representing the length of the longest increasing subsequence.
Constraints:

1 <= length(A) <= 2500
1 <= A[i] <= 2000
'''

class Solution:
	# @param A : tuple of integers
	# @return an integer
	def lis(self, A):
        n = len(A)
        dp = [1 for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if A[i] > A[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
