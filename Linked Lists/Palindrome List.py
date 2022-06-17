"""
Given a singly linked list, determine if its a palindrome. Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
"""

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        slow = A
        fast = A
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        def reverseList(node):
            prev = None
            while node is not None:
                nNode = node.next
                node.next = prev
                prev = node
                node = nNode

            return prev

        slow.next = reverseList(slow.next)

        h1 = A
        h2 = slow.next

        while h2 is not None:
            if h1.val != h2.val:
                return 0
            h1 = h1.next
            h2 = h2.next

        return 1
