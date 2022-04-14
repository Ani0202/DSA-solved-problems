'''
Given an array of integers A, find and return the peak element in it.

An array element is peak if it is NOT smaller than its neighbors. 

For corner elements, we need to consider only one neighbor. 

For example, for input array {5, 10, 20, 15}, 20 is the only peak element.

Following corner cases give better idea about the problem.

1) If input array is sorted in strictly increasing order, the last element is always a peak element. 
For example, 5 is peak element in {1, 2, 3, 4, 5}.
2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 
10 is the peak element in {10, 9, 8, 7, 6}.
Note: It is guranteed that the answer is unique.




Input Format

The only argument given is the integer array A.
Output Format

Return the peak element.
Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        n = len(A)
        l = 0
        h = n-1
        
        
        while l<=h:
            m = (l+h)//2
            if m==0 and A[m]>=A[1]:
                return A[m]
            if m==n-1 and A[m]>=A[m-1]:
                return A[m]
            if A[m]>=A[m+1] and A[m]>=A[m-1]:
                return A[m]
            
            if A[m]<A[m-1]:
                h = m-1
                
            elif A[m]<A[m+1]:
                l = m+1