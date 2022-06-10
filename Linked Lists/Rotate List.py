'''
Given a list, rotate the list to the right by k places, where k is non-negative.
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @param B : integer
	# @return the head node in the linked list
    def rotateRight(self, A, B):
		node = A
		count = 1
		while node.next != None:
			node = node.next
			count += 1

		B = B%count
		if B == 0:
			return A
		
		top = A
		for i in range(count - B - 1):
			top = top.next

		node.next = A
		head = top.next
		top.next = None

		return head