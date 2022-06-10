'''
Problem Description
 
 

You are given two numbers A and B.

You have to add them without using arithmetic operators and return their sum.



Problem Constraints
1 <= A, B <= 109


Input Format
The first argument is the integer A. The second argument is the integer B.


Output Format
Return a single integer denoting their sum.
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def addNumbers(self, A, B):
        while (B>0):
            carry=A&B
            A^=B
            B=carry<<1
        return A
