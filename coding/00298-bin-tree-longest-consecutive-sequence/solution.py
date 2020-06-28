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
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def plen(node):
            if node.left:
                left, lbest = plen(node.left)
                if node.left.val != node.val+1:
                    left = 0
            else:
                left = lbest = 0

            if node.right:
                right, rbest = plen(node.right)
                if node.right.val != node.val+1:
                    right = 0
            else:
                right = rbest = 0

            curr = max(left+1, right+1)
            best = max(lbest, rbest, curr)
            return curr, best

        if not root:
            return 0
        else:
            return plen(root)[1]
