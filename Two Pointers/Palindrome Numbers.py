"""
Given two integers A and B which represent an integer range [A, B].
Find the maximum number of distinct palindromic integers we can take from the given range,
such that the absolute difference between any two integers doesn't exceed C.


Problem Constraints
1 <= A <= B <= 105
1 <= C <= 105


Input Format
The first argument is an integer A.
The second argument is an integer B.
The third argument is an integer C.


Output Format
Return an integer.
"""


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        palind = list()
        i = A
        while i <= B:
            j = str(i)
            if j == j[::-1]:
                palind.append(i)

            i += 1

        if len(palind) < 2:
            return len(palind)

        ans = 1
        c = 1
        m = 0
        i = 1
        while i < len(palind):
            if palind[i] - palind[m] <= C:
                c += 1
            else:
                c += 1
                while palind[i] - palind[m] > C:
                    c -= 1
                    m += 1
            ans = max(ans, c)
            i += 1

        return ans