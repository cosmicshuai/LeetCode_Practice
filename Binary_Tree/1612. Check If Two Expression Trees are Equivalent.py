# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        def getVals(node):
            ans = {}
            def dfs(node, sign):
                if not node:
                    return
                
                if not node.val in "+-":
                    ans[node.val] = ans.get(node.val, 0) + sign * 1
                elif node.val == "+":
                    dfs(node.left, sign)
                    dfs(node.right, sign)
                else:
                    dfs(node.left, sign)
                    dfs(node.right, -sign)

                

            dfs(node, 1)
            keys = list(ans.keys())
            keys.sort()
            res = []
            for k in keys:
                res.append(k + "*" + str(ans[k]))
            return "+".join(res)
        
        ans1 = getVals(root1)
        ans2 = getVals(root2)
        return ans1 == ans2