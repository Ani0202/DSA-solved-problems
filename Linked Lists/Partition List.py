"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        sHead = None

        sTail = None
        bHead = None
        bTail = None

        while A:
            if A.val < B:
                if sHead is None:
                    sHead = A
                    sTail = A
                else:
                    sTail.next = A
                    sTail = sTail.next

            else:
                if bHead is None:
                    bHead = A
                    bTail = A
                else:
                    bTail.next = A
                    bTail = bTail.next

            t = A.next
            A.next = None
            A = t

        if sHead:
            sTail.next = bHead
            return sHead

        return bHead

