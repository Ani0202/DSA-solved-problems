'''
Problem Description

Given a linked list A , reverse the order of all nodes at even positions.



Problem Constraints
1 <= Size of linked list <= 100000



Input Format
First and only argument is the head of the Linked-List A.



Output Format
Return the head of the new linked list.
'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        e = 1
        node = A
        nums = []
        while node:
            if e == 0:
                nums.append(node)
            node = node.next
            e = (e+1)%2

        e = 1
        node = A
        while node:
            if e == 0:
                node.val = nums.pop()

            node = node.next
            e = (e+1)%2

        return A

