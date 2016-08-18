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
    def _is_valid(self, node):
        """ Returns (is_valid, min, max) """
        if not node:
            return True, None, None

        lvalid, lmin, lmax = self._is_valid(node.left)
        if not lvalid:
            return False, None, None

        rvalid, rmin, rmax = self._is_valid(node.right)
        if not rvalid:
            return False, None, None

        if lmax is not None:
            if lmax >= node.val:
                return False, None, None
            else:
                _min = lmin
        else:
            _min = node.val

        if rmin is not None:
            if rmin <= node.val:
                return False, None, None
            else:
                _max = rmax
        else:
            _max = node.val

        return True, _min, _max

    def isValidBST(self, root):
        """
        **ALL** left sub-trees should be strictly smaller
        **ALL** right sub-trees should be strictly larger

        :type root: TreeNode
        :rtype: bool
        """
        return self._is_valid(root)[0]
