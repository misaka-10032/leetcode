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
    def check(self, curr):
        if self.prev and self.prev.val >= curr.val:
            if self.first is None:
                self.first = self.prev
            self.second = curr
        self.prev = curr

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        curr = root
        self.prev = self.first = self.second = None
        while curr:
            if curr.left is None:
                self.check(curr)
                curr = curr.right
            else:
                rightmost = curr.left
                while rightmost.right and rightmost.right is not curr:
                    rightmost = rightmost.right
                if rightmost.right is None:  # not yet threaded
                    rightmost.right = curr
                    curr = curr.left
                else:
                    self.check(curr)
                    rightmost.right = None
                    curr = curr.right
        assert self.first
        assert self.second
        self.first.val, self.second.val = self.second.val, self.first.val
