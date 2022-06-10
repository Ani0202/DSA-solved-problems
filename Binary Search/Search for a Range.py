'''
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].




Input Format

The first argument given is the integer array A.
The second argument given is the integer B.
Output Format

 Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].
Constraints

1 <= N <= 10^6
1 <= A[i], B <= 10^9
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        l = 0
        h = len(A)-1
        start = -1
        end = -1
        while l <= h:
            m = l + (h-l)//2
            if A[m] == B:
                start = m
                end = m
                while start != 0 and A[start-1] == B:
                    start -= 1

                while end != len(A)-1 and A[end+1] == B:
                    end += 1

                break

            elif A[m] > B:
                h = m-1
            else:
                l = m+1

        return [start, end]