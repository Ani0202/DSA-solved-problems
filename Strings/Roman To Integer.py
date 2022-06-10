'''
Given a string A representing a roman numeral.

Convert A into integer.

A is guaranteed to be within the range from 1 to 3999.




Input Format

The only argument given is string A.
Output Format

Return an integer which is the integer verison of roman numeral string.
'''

class Solution:
	# @param A : string
	# @return an integer
	def romanToInt(self, A):
        romToInt = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(A)-1):
            if romToInt[A[i]] < romToInt[A[i+1]]:
                ans -= romToInt[A[i]]
            else:
                ans += romToInt[A[i]]
        ans += romToInt[A[-1]]

        return ans