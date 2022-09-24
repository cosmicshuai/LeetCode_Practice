# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(root, sumOf, path):
            if not root:
                return
            if not root.right and not root.left:
                if sumOf + root.val == targetSum:
                    res.append(path + [root.val])
            
            if root.left:
                dfs(root.left, sumOf + root.val, path + [root.val])
                
            if root.right:
                dfs(root.right, sumOf + root.val, path + [root.val])
                
        dfs(root, 0, [])
        return res