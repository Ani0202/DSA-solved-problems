'''
Problem Description

Given an integer A, return the number of trailing zeroes in A!.

Note: Your solution should be in logarithmic time complexity.



**Problem Constraints**
1 <= A <= 10000



**Input Format**
First and only argumment is integer A.



**Output Format**
Return an integer, the answer to the problem.
'''

class Solution:
	# @param A : integer
	# @return an integer
	def trailingZeroes(self, A):
        ans = 0
        d = 5
        while d <= A:
            ans += A//d
            d *= 5

        return ans
