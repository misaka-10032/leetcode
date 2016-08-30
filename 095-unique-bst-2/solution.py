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


def deep_copy(root, offset=0):
    if root is None:
        return None
    new = TreeNode(root.val + offset)
    new.left = deep_copy(root.left, offset)
    new.right = deep_copy(root.right, offset)
    return new


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        forest = [[] for _ in xrange(n+1)]
        forest[0] = [None]
        forest[1] = [TreeNode(1)]
        # build bst with k nodes
        for k in xrange(2, n+1):
            # iterate roots
            for i in xrange(1, k+1):
                root = TreeNode(i)
                # iterate left trees
                for left in forest[i-1]:
                    root.left = left
                    for right in forest[k-i]:
                        root.right = deep_copy(right, i)
                        # working on trees with k nodes
                        forest[k].append(deep_copy(root))
        return forest[n]
