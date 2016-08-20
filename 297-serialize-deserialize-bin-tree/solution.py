# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.val == other.val


import json
from collections import deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return json.dumps([])
        vals = []
        Q = deque()
        Q.append(root)
        while Q:
            node = Q.popleft()
            if node:
                vals.append(node.val)
                Q.append(node.left)
                Q.append(node.right)
            else:
                vals.append(None)
        return json.dumps(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = json.loads(data)
        if not vals:
            return None
        Q = deque()
        root = TreeNode(vals[0])
        Q.append(root)
        i = 1
        while i < len(vals):
            parent = Q.popleft()
            if vals[i] is not None:
                left = TreeNode(vals[i])
                parent.left = left
                Q.append(left)
            i += 1
            if vals[i] is not None:
                right = TreeNode(vals[i])
                parent.right = right
                Q.append(right)
            i += 1
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
