"""
Given an array of integers A and an integer B.

Find the total number of subarrays having bitwise XOR of all elements equals to B.



Problem Constraints
1 <= length of the array <= 105

1 <= A[i], B <= 109



Input Format
The first argument given is the integer array A.

The second argument given is integer B.



Output Format
Return the total number of subarrays having bitwise XOR equals to B.
"""


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        ans = 0
        xArr = [0 for _ in range(n)]
        hmap = dict()
        xArr[0] = A[0]

        for i in range(1, n):
            xArr[i] = xArr[i - 1] ^ A[i]

        for i in range(n):
            tmp = B ^ xArr[i]

            if tmp in hmap.keys():
                ans = ans + (hmap[tmp])
            if xArr[i] == B:
                ans += 1

            hmap[xArr[i]] = hmap.get(xArr[i], 0) + 1

        return ans
