# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.S = deque()
        curr = root
        while curr:
            self.S.append(curr)
            curr = curr.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.S)

    def next(self):
        """
        :rtype: int
        """
        top = self.S.pop()
        curr = top.right
        while curr:
            self.S.append(curr)
            curr = curr.left
        return top.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())