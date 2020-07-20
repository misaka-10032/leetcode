#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _traverse(self, node: Optional[TreeNode], lval: int, rval: int,
                  curr_sum: List[int]):
        if not node:
            return
        self._traverse(node.left, lval, rval, curr_sum)
        if lval <= node.val <= rval:
            curr_sum[0] += node.val
        if node.val < rval:
            self._traverse(node.right, lval, rval, curr_sum)

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        final_sum = [0]
        explore_right = root.val < R
        self._traverse(root, L, R, final_sum)
        return final_sum[0]
