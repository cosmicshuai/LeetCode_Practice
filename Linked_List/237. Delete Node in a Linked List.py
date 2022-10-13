# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
copy the value from next node, then skip the next node
"""
class Solution:
    def deleteNode(self, node:ListNode):
        node.val  = node.next.val
        node.next = node.next.next