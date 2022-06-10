'''
Problem Description
 
 

A conveyor belt has packages that must be shipped from one port to another within B days.

The ith package on the conveyor belt has a weight of A[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within B days.



Problem Constraints
1 <= B <= |A| <= 5 * 105
1 <= A[i] <= 105


Input Format
First argument is array of integers A denoting the weights.

Second argument is the integer B denoting the number of days. 



Output Format
Return the least weight capacity of the ship.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        h = sum(A)
        l = max(A)
        ans = -1
        while l<=h:
            m = l + (h-l)//2

            days = 1
            s = 0
            isValid = True
            for i in range(len(A)):
                s += A[i]
                if s > m:
                    days += 1
                    s = A[i]

                if days > B:
                    isValid = False
                    break

            if isValid:
                ans = m
                h = m-1
            else:
                l = m+1

        return ans

