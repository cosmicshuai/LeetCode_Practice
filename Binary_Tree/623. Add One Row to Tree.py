# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node

        def dfs(root, level):
            if not root:
                return 

            if level == depth - 1:
                if root.left:
                    node = TreeNode(val)
                    node.left = root.left
                    root.left = node
                else:
                    node = TreeNode(val)
                    root.left = node
                
                if root.right:
                    node = TreeNode(val)
                    node.right = root.right
                    root.right = node
                else:
                    node = TreeNode(val)
                    root.right = node

                return
            else:
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)

        dfs(root, 1)
        return root