# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional
class Solution:
    @classmethod
    def reverseNodes(cls, queue):
        n = len(queue)
        i, j = 0, n - 1
        while i < j:
            queue[i].val, queue[j].val = queue[j].val, queue[i].val
            i += 1
            j -= 1
    
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        isOdd = False
        queue = deque([root])
        

            
        while queue:
            level = deque()
            if isOdd:
                Solution.reverseNodes(queue)
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                    
            queue = level
            isOdd = not isOdd
            
        return root