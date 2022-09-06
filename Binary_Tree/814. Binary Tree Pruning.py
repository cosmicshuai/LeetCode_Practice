from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use devide and conquer to solve this problem
        def dfs(root):
            if not root:
                return True
            left = dfs(root.left)
            right = dfs(root.right)
            if left:
                root.left = None
            if right:
                root.right = None
            if root.val == 0 and left and right:
                return True
            return False
        
        #tricky part, if the root is zero tree, return None
        return root if not dfs(root) else None