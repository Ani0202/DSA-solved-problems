'''
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.
'''

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        n = len(A)
        for i in range(0, n):
            A[i] += (A[A[i]] % n) * n
        for i in range(0, n):
            A[i] = int(A[i] / n)