#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traverse(self, node: TreeNode, max_diff: List[int]) -> Tuple[int, int]:
        # Updates max_diff and returns the min and the max of the subtree.
        if not node.left and not node.right:
            return node.val, node.val

        min_val = max_val = node.val
        for child in (node.left, node.right):
            if not child:
                continue
            min_child, max_child = self._traverse(child, max_diff)
            min_val = min(min_val, min_child)
            max_val = max(max_val, max_child)
            diff1 = abs(node.val - min_val)
            diff2 = abs(node.val - max_val)
            max_diff[0] = max(max_diff[0], diff1, diff2)
        return min_val, max_val

    def maxAncestorDiff(self, root: TreeNode) -> int:
        max_diff = [0]
        self._traverse(root, max_diff)
        return max_diff[0]
