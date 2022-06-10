'''
You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE:  if B > N, return an empty array.



Input Format
First argument is an integer array A

Second argument is an integer B.



Output Format
Return an integer array.
'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        if B > len(A):
            return []

        ans = []
        count = dict()
        for i in range(B):
            count[A[i]] = count.get(A[i], 0) +1

        i = 0
        j = B-1
        while j < len(A):
            a = 0
            ans.append(len(count))
            count[A[i]] -= 1
            if count[A[i]] == 0:
                del count[A[i]]
            if j+1 < len(A):
                count[A[j+1]] = count.get(A[j+1], 0) + 1

            i += 1
            j += 1

        return ans