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


def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    if not p and q or p and not q:
        return False
    if p.val != q.val:
        return False
    if not isSameTree(p.left, q.left):
        return False
    if not isSameTree(p.right, q.right):
        return False
    return True


class Solution(object):
    def flip(self, old):
        if not old:
            return None
        new = TreeNode(old.val)
        new.left = self.flip(old.right)
        new.right = self.flip(old.left)
        return new

    def isSymmetric(self, root):
        """
        See if flip == old

        The other quicker way is to check palindrome in each layer

        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        flip = self.flip(root)
        return isSameTree(root, flip)
