# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPseudoPalin(mask):
            return bin(mask).count('1') <= 1
             
        
        
        self.ans = 0
        def dfs(mask, root):
            if not root:
                return
            if not root.left and not root.right:
                if isPseudoPalin(mask ^ 1 << root.val):
                    self.ans += 1
                return
                    
            if root.left:
                dfs(mask ^ 1 << root.val, root.left)
            if root.right:
                dfs(mask ^ 1 << root.val, root.right)
            
        dfs(0, root)
        
        return self.ans