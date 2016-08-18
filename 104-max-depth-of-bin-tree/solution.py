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


class Solution(object):
    def probe(self, node, level):
        if not node:
            return level
        return max(self.probe(node.left, level+1),
                   self.probe(node.right, level+1))

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.probe(root, 0)
