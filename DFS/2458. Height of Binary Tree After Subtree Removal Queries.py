# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict
from typing import List, Optional
"""
Initial idea: use dfs to take every query, compute the result, easy to write the code, but will get TLE.
Optimization: we can memorize the level of each node, nodes in each level and the deepest level of each node can achieve.  the result of a query depends on the max level achieved by others nodes in the same level
Further optimization: traverse each level takes O(N) time, we can sort first, thus we only need to compare the first two nodes in each level
"""
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        levels = defaultdict(list)
        pos = {}
        def dfs(root, lvl):
            if not root:
                return lvl
            pos[root.val] = lvl
            
            l = dfs(root.left, lvl + 1) if root.left else lvl
            r = dfs(root.right, lvl + 1)  if root.right else lvl
            t = max(l, r)
            levels[lvl].append((t, root.val))
            return t
        dfs(root, 0)

        for val in levels.values():
            val.sort(reverse=True)

        ans = []
        for i in queries:
            lvl = pos[i]
            t = 0
            tmp = levels[lvl]
            if len(tmp) == 1:
                ans.append(lvl - 1)
            else:
                if tmp[0][1] == i:
                    ans.append(tmp[1][0])
                else:
                    ans.append(tmp[0][0])
        return ans