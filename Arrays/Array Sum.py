'''
Problem Description
 
 

You are given two numbers represented as integer arrays A and B, where each digit is an element.

You have to return an array which representing the sum of the two given numbers.

The last element denotes the least significant bit, and the first element denotes the most significant bit.



Problem Constraints
1 <= |A|, |B| <= 105
0 <= Ai, Bi <= 9


Input Format
The first argument is an integer array A. The second argument is an integer array B.


Output Format
Return an array denoting the sum of the two numbers.
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def addArrays(self, A, B):
        if len(B) > len(A):
            A, B = B, A

        ans = []
        n = len(A)
        m = len(B)
        i = n-1
        j = m-1
        carry = 0
        while i >= 0:
            s = A[i]
            i -= 1
            if j >= 0 :
                s += B[j]
                j -= 1
            s += carry
            ans.append(s%10)
            carry = s//10

        if carry:
            ans.append(carry)
        return reversed(ans)