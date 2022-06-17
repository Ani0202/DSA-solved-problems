"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the first node in the cycle in the linked list
    def detectCycle(self, A):
        if A.next is None:
            return
        slow = A.next
        fast = A.next.next
        while slow is not None and fast is not None and fast.next is not None:
            if slow == fast:
                slow = A
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
            slow = slow.next
            fast = fast.next.next

        return
