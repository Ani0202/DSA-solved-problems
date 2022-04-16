'''
Problem Description

Given an integer array A of size N.

You need to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine and return this value.

For example, if A = [3, 4, 5] :

Subarray    Operation   Result
3       None            3
4       None            4
5       None            5
3,4   3 XOR 4         7
4,5   4 XOR 5         1
3,4,5    3 XOR 4 XOR 5   2

Now we take the resultant values and XOR them together:

3 ⊕ 4 ⊕ 5 ⊕ 7 ⊕ 1⊕ 2 = 6 we will return 6.



Problem Constraints
1 <= N <= 105

1 <= A[i] <= 108



Input Format
First and only argument is an integer array A.



Output Format
Return a single integer denoting the value as described above.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        if n%2 == 0:
            return 0
        ans = 0
        for i in range(0, n, 2):
            ans ^= A[i]
        return ans
            

