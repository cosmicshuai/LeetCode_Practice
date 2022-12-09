from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, max_, min_):
            if not node:
                return
            self.ans = max(self.ans, abs(max_ - node.val))
            self.ans = max(self.ans, abs(min_ - node.val))
            max_ = max(max_, node.val)
            min_ = min(min_, node.val)
            dfs(node.left, max_, min_)
            dfs(node.right, max_, min_)
        dfs(root, root.val, root.val)
        return self.ans