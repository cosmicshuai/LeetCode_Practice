# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return root
            if not root.left and not root.right:
                return root
            
            right = dfs(root.right)
            left = dfs(root.left)
            root.left = right
            root.right = left
            return root
        
        dfs(root)
        return root
            