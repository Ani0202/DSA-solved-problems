'''
Problem Description
 
 

Given a string A. The string contains some words separated by spaces.
Return the number of words in the given string.


Problem Constraints
1 <= |A| <= 105
Ai = { lowercase English letters or spaces}


Input Format
The first and only argument is a string A.


Output Format
Return an integer.
'''

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        t = ''
        i = 0
        ans = 0
        while i < len(A):
            if A[i] == ' ':
                if len(t) > 0:
                    ans += 1
                t = ''
            else:
                t += A[i]

            i += 1

        if len(t) > 0:
            ans += 1

        return ans
