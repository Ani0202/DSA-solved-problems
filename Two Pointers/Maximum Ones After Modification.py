"""
Given a binary array A and a number B, we need to find length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.



Problem Constraints
 1 <= N, B <= 105

 A[i]=0 or A[i]=1



Input Format
First argument is an binary array A.

Second argument is an integer B.



Output Format
Return a single integer denoting the length of the longest subsegment of ‘1’s possible by changing at most B ‘0’s.
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        i = 0
        j = 0
        ans = 0
        while j < len(A):
            if A[j] == 0:
                if B != 0:
                    B -= 1
                else:
                    while i < j:
                        if A[i] == 0:
                            i += 1
                            break
                        i += 1

            ans = max(ans, j - i + 1)
            j += 1

        return ans