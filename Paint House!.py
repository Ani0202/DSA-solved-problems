'''
There are a row of N houses, each house can be painted with one of the three colors: red, blue or green.

The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a N x 3 cost matrix A.

For example, A[0][0] is the cost of painting house 0 with color red; A[1][2] is the cost of painting house 1 with color green, and so on.

Find the minimum total cost to paint all houses.



Problem Constraints
1 <= N <= 105

1 <= A[i][j] <= 103



Input Format
First and only argument is an 2D integer matrix A of size N x 3 denoting the cost to paint the houses.



Output Format
Return an integer denoting the minimum total cost to paint all houses.
'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        cost = A[0]
        R = A[0][0]
        G = A[0][1]
        B = A[0][2]

        for i in range(1, n):
            cost[0] = A[i][0] + min(G, B)
            cost[1] = A[i][1] + min(B, R)
            cost[2] = A[i][2] + min(R, G)
            R = cost[0]
            G = cost[1]
            B = cost[2]

        return min(cost)
