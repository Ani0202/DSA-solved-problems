"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        carry = 0

        head = node = None
        while A is not None or B is not None:
            s = carry
            if A is not None:
                s += A.val
                A = A.next
            if B is not None:
                s += B.val
                B = B.next
            v = s % 10
            carry = s // 10
            if node is None:
                head = node = ListNode(v)
            else:
                node.next = ListNode(v)
                node = node.next

        if carry:
            node.next = ListNode(carry)

        return head
