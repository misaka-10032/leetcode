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


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.G = self._traverse(root)
        self.last = root
        self.curr = None
        while self.last and self.last.right:
            self.last = self.last.right

    def _traverse(self, root):
        if not root:
            return
        for node in self._traverse(root.left):
            yield node
        yield root
        for node in self._traverse(root.right):
            yield node

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr is not self.last

    def next(self):
        """
        :rtype: int
        """
        self.curr = self.G.next()
        return self.curr.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())