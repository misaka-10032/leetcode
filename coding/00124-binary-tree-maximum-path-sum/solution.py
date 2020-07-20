#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _max_path_sum(self, node: Optional[TreeNode], result: List[int]) -> int:
        # Find the max path sum that includes `node`. The return value is the max sum
        # with this `node` not being the top node. `result` tracks the possibility of
        # this node being the "top" node.
        if not node:
            return 0
        left_sum = self._max_path_sum(node.left, result)
        right_sum = self._max_path_sum(node.right, result)
        # `tot1` represents the best sum with `node` being the top. Both `left` and
        # `right` can be selected because `node` is top.
        tot1 = node.val + max(0, left_sum) + max(0, right_sum)
        result[0] = max(result[0], tot1)
        # `tot2` represents the best sum with `node` NOT being the top. Only one child
        # can be selected because `node` is not top.
        tot2 = node.val + max(0, left_sum, right_sum)
        return tot2

    def maxPathSum(self, root: TreeNode) -> int:
        result = [root.val]
        self._max_path_sum(root, result)
        return result[0]
