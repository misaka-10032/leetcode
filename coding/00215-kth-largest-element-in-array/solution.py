#!/usr/bin/env python3
# encoding: utf-8

import random
from typing import List


class Solution:
    def _pivot(self, nums: List[int], start: int, end: int) -> int:
        # Put nums[start] to its right place. Keep the smaller (or equal) numbers
        # on its left and the bigger numbers on the right. Return its index (order).
        assert start < end
        if start + 1 == end:
            return start
        val = nums[start]
        # The first gt after start
        gt = start + 1
        while gt < end and nums[gt] <= val:
            gt += 1
        # The first le after gt
        le = gt + 1
        while le < end:
            while le < end and nums[le] > val:
                le += 1
            if le < end:
                nums[gt], nums[le] = nums[le], nums[gt]
                gt += 1
                le += 1
        pivot_idx = gt - 1
        nums[start], nums[pivot_idx] = nums[pivot_idx], val
        return pivot_idx

    def _find_kth(self, nums: List[int], k: int, start: int, end: int) -> int:
        target_idx = random.randrange(start, end)
        nums[start], nums[target_idx] = nums[target_idx], nums[start]
        idx = self._pivot(nums, start, end)
        if k > idx:
            return self._find_kth(nums, k, idx + 1, end)
        elif k < idx:
            return self._find_kth(nums, k, start, idx)
        else:  # k == idx
            return nums[k]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self._find_kth(nums, len(nums) - k, 0, len(nums))
