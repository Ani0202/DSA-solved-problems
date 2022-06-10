'''
Problem Description
 
 

Given a large number represent in the form of an integer array A, where each element is a digit.

You have to find whether there exists any permutation of the array A such that the number becomes divisible by 60.

Return 1 if it exists, 0 otherwise.



Problem Constraints
1 <= |A| <= 105
0 <= Ai <= 9


Input Format
The first argument is an integer array A.


Output Format
Return a single integer '1' if there exists a permutation, '0' otherwise.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):
        if A == [0]:
            return 1
        sumDigits = 0
        divTen = 0
        divFour = 0
        for i in range(len(A)):
            sumDigits += A[i]
            if divTen == 0 and A[i] == 0:
                divTen = 1
            elif divFour == 0 and A[i]%2==0:
                divFour = 1

        if sumDigits%3 == 0 and divFour and divTen:
            return 1
        else:
            return 0