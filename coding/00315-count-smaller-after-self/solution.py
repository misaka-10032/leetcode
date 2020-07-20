#!/usr/bin/env python3
# encoding: utf-8

import bisect
import dataclasses
from typing import List, Optional


@dataclasses.dataclass
class TreeNode:
    start: int
    end: int
    sum: int = 0
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None


class SegTree:
    def __init__(self, length: int):
        self._counters = [0] * length
        self._root = self._build_tree(0, length)

    def _build_tree(self, start: int, end: int):
        if start + 1 == end:
            return TreeNode(start, end)
        mid_idx = (start + end) // 2
        left = self._build_tree(start, mid_idx)
        right = self._build_tree(mid_idx, end)
        return TreeNode(start, end, left=left, right=right)

    def _range_sum(self, node: TreeNode, start: int, end: int):
        if node.start == start and node.end == end:
            return node.sum
        node_mid = (node.start + node.end) // 2
        tot = 0
        if start < node_mid:
            tot += self._range_sum(node.left, start, min(node_mid, end))
        if end > node_mid:
            tot += self._range_sum(node.right, max(node_mid, start), end)
        return tot

    def range_sum(self, start: int, end: int):
        if start == end:
            return 0
        if start + 1 == end:
            return self._counters[start]
        return self._range_sum(self._root, start, end)

    def inc(self, idx: int):
        self._counters[idx] += 1
        node = self._root
        while node:
            node.sum += 1
            node_mid = (node.start + node.end) // 2
            if idx < node_mid:
                node = node.left
            else:
                node = node.right


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        sorted_unique_nums = sorted(set(nums))
        # A seg tree that maintains the counters for the indices in `sorted_unique_nums`.
        seg_tree_counters = SegTree(len(sorted_unique_nums))
        # The result counters.
        result_counters = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            # Find the idx of nums[i] in the seg tree.
            seg_tree_idx = bisect.bisect_left(sorted_unique_nums, nums[i])
            # All the elements on its left should be counted.
            result_counters[i] = seg_tree_counters.range_sum(0, seg_tree_idx)
            # Maintain the counters in the tree.
            seg_tree_counters.inc(seg_tree_idx)
        return result_counters
