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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        all = []
        level = [root]
        order = True
        while level:
            # no need to copy
            all.append(map(lambda x: x.val, level if order else reversed(level)))
            next = []
            for node in level:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            level = next
            order = not order
        return all
