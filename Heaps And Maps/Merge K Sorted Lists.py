'''
Merge k sorted linked lists and return it as one sorted list.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        heap = []
        for i in range(len(A)):
            heapq.heappush(heap, (A[i].val, A[i]))
        ans =  node = None
        while len(heap):
            i,j = heapq.heappop(heap)
            if j.next != None:
                heapq.heappush(heap, (j.next.val, j.next))
            if node == None:
                node = ans = j
            else:
                node.next = j
                node = node.next
        return ans