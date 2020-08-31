#!/usr/bin/env python3
# encoding: utf-8

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traverse(self, node: Optional['TreeNode'],
                  prev: Optional['TreeNode']) -> 'TreeNode':
        if not node:
            return None
        if prev:
            prev.left = None
            prev.right = node
        left_node = node.left
        right_node = node.right
        left_last = self._traverse(left_node, node)
        right_last = self._traverse(right_node, left_last)
        return right_last or left_last or node

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self._traverse(root, None)
