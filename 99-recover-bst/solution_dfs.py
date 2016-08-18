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
    def _find(self, node):
        if node is None:
            return
        self._find(node.left)

        if self.prev and self.prev.val >= node.val:
            if self.first is None:
                self.first = self.prev
            self.second = node
        self.prev = node

        self._find(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = self.first = self.second = None
        self._find(root)
        assert self.first
        assert self.second
        self.first.val, self.second.val = self.second.val, self.first.val
