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
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def find(node, offset):
            """ Returns size of sub-tree.
                Terminate early if kth is found. """
            if not node:
                return offset
            if kth.val is not None:
                # found
                return -inf
            left = find(node.left, offset)
            curr = left + 1
            if curr == k:
                kth.val = node.val
            return find(node.right, curr)
        inf = 999999999
        kth = TreeNode(None)
        find(root, 0)
        return kth.val
