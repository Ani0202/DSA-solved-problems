"""
Implement atoi to convert a string to an integer.
"""


class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        A = A.strip().split()
        if A is None:
            return 0
        A = A[0]
        i = 0
        neg = False
        if A[0] == '+':
            i += 1
        elif A[0] == '-':
            neg = True
            i += 1

        res = 0
        while i < len(A) and A[i].isdigit():
            res = res * 10 + int(A[i])
            i += 1

        if neg:
            if -res < -2 ** 31:
                return -2 ** 31
            else:
                return -res
        else:
            if res > 2 ** 31 - 1:
                return 2 ** 31 - 1
            else:
                return res
