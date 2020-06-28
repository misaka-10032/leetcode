# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* Find the closest on the path
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        best = None
        curr = root
        while curr:
            if best is None or abs(curr.val - target) < abs(best - target):
                best = curr.val

            if curr.val == target:
                return curr.val
            elif target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return best
