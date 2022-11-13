# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
from typing import Optional
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def numOfSwap(arr):
            nums = [i for i in arr]
            nums.sort()
            mem = {}
            for i, v in enumerate(nums):
                mem[v] = i
            
            idxArr = []
            for v in arr:
                idxArr.append(mem[v])
            
            n = len(nums)
            i = 0
            cnt = 0
            while i < n:
                while i < n and idxArr[i] == i:
                    i += 1
                if i == n:
                    break
                cur = idxArr[i]
                target = idxArr[idxArr[i]]
                idxArr[i], idxArr[cur] = target, cur
                cnt += 1
            return cnt

        queue = deque([root])
        ans = 0
        while queue:
            t = [node.val for node in queue]
            ans += numOfSwap(t)
            l = len(queue)
            for _ in range(l):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return ans



