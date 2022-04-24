'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note: You have to modify the array A to contain the merge of A and B. Do not output anything in your code.

TIP: C users, please malloc the result into a new array and return the result.

If the number of elements initialized in A and B are m and n respectively, the resulting size of array A after your code is executed should be 
m + n
'''

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    def merge(self, A, B):
        i = 0
        for j in B:
            while i < len(A) and A[i] <= j:
                i += 1

            A.insert(i, j)

        return A
