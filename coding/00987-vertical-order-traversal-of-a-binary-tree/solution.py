#!/usr/bin/env python3
# encoding: utf-8


import collections
from typing import DefaultDict, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traverse(self, node: Optional[TreeNode], x: int, y: int,
                  x_to_y_to_vals: DefaultDict[int, DefaultDict[int, int]]):
        if not node:
            return
        x_to_y_to_vals[x][y].append(node.val)
        self._traverse(node.left, x - 1, y - 1, x_to_y_to_vals)
        self._traverse(node.right, x + 1, y - 1, x_to_y_to_vals)

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        x_to_y_to_vals = collections.defaultdict(
            lambda: collections.defaultdict(list))
        self._traverse(root, 0, 0, x_to_y_to_vals)
        result = []
        for x in sorted(x_to_y_to_vals.keys()):
            col = []
            y_to_vals = x_to_y_to_vals[x]
            for y in sorted(y_to_vals.keys(), reverse=True):
                col.extend(sorted(y_to_vals[y]))
            result.append(col)
        return result
