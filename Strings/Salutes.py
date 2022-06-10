'''
Problem Description
 
 

In a long hallway some soldiers are walking from left to right and some from right to left all at the same speed.

Every time while walking they cross through another soldier they salute and move ahead.

Given a string A of length N showing the soldiers' direction they are walking. 
'<' denotes a soldier is walking from right to left, and '>' denotes a soldier is walking from left to right. 
Return the number of Salutes done.



Problem Constraints
1 <= N <= 105
A = {'<', '>'}


Input Format
The first argument is a string A.


Output Format
Return a single integer denoting the number of salutes done.
'''

class Solution:
    # @param A : string
     # @return an long
    def countSalutes(self, A):
        r = 0
        ans = 0
        for i in range(len(A)):
            if A[i] == '>':
                r += 1
            else:
                ans += r

        return ans
