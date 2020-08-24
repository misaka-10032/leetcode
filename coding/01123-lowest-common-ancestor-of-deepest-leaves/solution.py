#!/usr/bin/env python3
# encoding: utf-8

"""Sol 2: one-pass"""

from typing import Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traverse(self, node: TreeNode) -> Tuple[int, TreeNode]:
        if not node.left and not node.right:
            return 1, node
        if node.left:
            left_height, left_lca = self._traverse(node.left)
        else:
            left_height = 0
        if node.right:
            right_height, right_lca = self._traverse(node.right)
        else:
            right_height = 0
        if left_height > right_height:
            return left_height + 1, left_lca
        elif left_height < right_height:
            return right_height + 1, right_lca
        else:
            return left_height + 1, node

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self._traverse(root)[1]
