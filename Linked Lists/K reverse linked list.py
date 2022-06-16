"""
Given a singly linked list and an integer K, reverses the nodes of the

list K at a time and returns modified linked list.

NOTE : The length of the list is divisible by K
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
    def reverseList(self, A, B):
        curr = A

    prev = None
    nNode = None

    k = 0
    while curr is not None and k < B:
        nNode = curr.next
        curr.next = prev
        prev = curr
        curr = nNode
        k += 1

    if curr is not None:
        A.next = self.reverseList(curr, B)

    return prev




