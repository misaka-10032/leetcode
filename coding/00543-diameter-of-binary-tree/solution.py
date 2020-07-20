#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _find_longest_path(self, node: Optional[TreeNode], longest: List[int]) -> int:
        # Finds the longest path within the subtree of `node`. The return value
        # is the height of `node`. The longest path within the subtrees is tracked
        # in `longest`.
        if not node:
            return 0
        left_height = self._find_longest_path(node.left, longest)
        right_height = self._find_longest_path(node.right, longest)
        height = max(left_height, right_height) + 1
        path_length = left_height + right_height
        longest[0] = max(longest[0], path_length)
        return height

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        longest = [0]
        self._find_longest_path(root, longest)
        return longest[0]
