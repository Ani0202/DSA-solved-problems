"""
Given an integer array A and two integers B and C.

You need to find the number of subarrays in which the number of occurrences of B is equal to number of occurrences of C.

NOTE: Don't count empty subarrays.



Problem Constraints
1 <= |A| <= 104

1 <= A[i], B, C <= 108

 B != C



Input Format
First argument is an integer array A.

Second argument is an integer B.

Third argument is an integer C.



Output Format
Return an integer denoting the number of subarrays in which the number of occurrences of B is equal to number of occurrences of C.
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        countB = [0 for i in range(n)]
        countC = [0 for i in range(n)]
        m = dict()

        for i in range(n):
            if A[i] == B:
                if i != 0:
                    countB[i] = countB[i - 1] + 1
                else:
                    countB[i] = 1
            else:
                if i != 0:
                    countB[i] = countB[i - 1]
                else:
                    countB[i] = 0

            if A[i] == C:
                if i != 0:
                    countC[i] = countC[i - 1] + 1
                else:
                    countC[i] = 1
            else:
                if i != 0:
                    countC[i] = countC[i - 1]
                else:
                    countC[i] = 0

            m[countB[i] - countC[i]] = m.get(countB[i] - countC[i], 0) + 1

        result = m[0]
        for j in m:
            result += (m[j] * (m[j] - 1)) // 2

        return result
