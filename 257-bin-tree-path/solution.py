# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        @param {TreeNode} root
        @return {string[]}
        """
        def dfs(node):
            curr.append(node.val)
            if node.left is None and node.right is None:
                # copy curr
                res.append(list(curr))
            if node.left is not None:
                dfs(node.left)
            if node.right is not None:
                dfs(node.right)
            curr.pop()

        if not root:
            return []

        res = []
        curr = []
        dfs(root)
        return map(lambda l: '->'.join(map(str, l)), res)
