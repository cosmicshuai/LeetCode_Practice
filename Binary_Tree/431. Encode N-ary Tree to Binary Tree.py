
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import Optional


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root:
            return None
        node = TreeNode(root.val)
        n = len(root.children)
        chnodes = []
        for i in range(n):
            chnodes.append(self.encode(root.children[i]))
        if chnodes:
            node.left = chnodes[0]
            nex = node.left
            for i in range(1, n):
                nex.right = chnodes[i]
                nex = nex.right
        return node
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data:
            return None
        node = Node(data.val)
        children = []
        nex = None
        if data.left:
            children.append(self.decode(data.left))
            nex = data.left
        while nex and nex.right:
            children.append(self.decode(nex.right))
            nex = nex.right
        node.children = children
        return node