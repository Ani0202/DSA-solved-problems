"""
Sort a linked list using insertion sort.
"""


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        head = None

        while A:
            a = A.next
            if head is None or A.val <= head.val:
                A.next = head
                head = A
            else:
                curr = head
                while curr.next is not None and curr.next.val < A.val:
                    curr = curr.next
                A.next = curr.next
                curr.next = A

            A = a
        return head
