# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = deque([])
        cnt = 0
        t = ""
        for c in traversal:
            if c != "-":
                t += c
            else:
                if t != "":
                    nodes.append((int(t), cnt))
                    t = ""
                    cnt = 1
                else:
                    cnt += 1
        if t != "":
            nodes.append((int(t), cnt))

        def dfs():
            val, dp = nodes.popleft()
            node = TreeNode(val)
            if nodes and nodes[0][1] == dp + 1:
                node.left = dfs()
            if nodes and nodes[0][1] == dp + 1:
                node.right = dfs()    
            return node

        root = dfs()
        return root
        