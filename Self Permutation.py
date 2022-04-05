'''
Problem Description
 
 

You are given two strings A and B.
Check whether there exists any permutation of both A and B such that they are equal.

Return a single integer 1 if its exists, 0 otherwise.



Problem Constraints
1 <= |A|, |B| <= 105
Both strings contain only lowercase english alphabets.


Input Format
The first argument is the string A. The second argument is the string B.


Output Format
Return a single integer 1 if a permutation exists, 0 otherwise.
'''

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def permuteStrings(self, A, B):
        count = dict()
        if len(A) != len(B):
            return 0
        for i in A:
            count[i] = count.get(i, 0) + 1

        for i in B:
            if count.get(i, 0) == 0:
                return 0
            count[i] -= 1

        return 1