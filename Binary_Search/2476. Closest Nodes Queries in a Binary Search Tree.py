# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
import bisect
from typing import List, Optional
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nodes = []
        # use a inorder travesal to store the sorted array
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)
        dfs(root)
        ans = []
        for num in queries:
            t = [-1, -1]
            # find min_i, which is equal to put queies[i] at the most right place and keep the order, if idx is 0, means no element is equal or smaller than queies[i]
            idx = bisect.bisect(nodes, num)
            if idx > 0:
                t[0] = nodes[idx - 1]

            idx = bisect.bisect_left(nodes, num)
            if idx < len(nodes):
                t[1] = nodes[idx]
            ans.append(t)
            
        return ans
