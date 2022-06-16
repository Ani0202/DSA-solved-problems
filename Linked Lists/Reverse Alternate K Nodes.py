"""
Given a linked list A of length N and an integer B.

You need to reverse every alternate B nodes in the linked list A.



Problem Constraints
1 <= N <= 105
1<= Value in Each Link List Node <= 103
1 <= B <= N
N is divisible by B


Input Format
First argument is the head pointer of the linkedlist A.

Second argument is an integer B.



Output Format
Return the head pointer of the final linkedlist as described.
"""


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def solve(self, A, B):
        k = 0
        curr = A
        prev = None

        while curr is not None and k < B:
            nNode = curr.next
            curr.next = prev
            prev = curr
            curr = nNode
            k += 1

        if curr is not None:
            k = 0
            while curr is not None and k < B:
                A.next = curr
                A = curr
                curr = curr.next
                k += 1

        if curr is not None:
            A.next = self.solve(curr, B)

        return prev