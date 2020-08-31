#!/usr/bin/env python3
# encoding: utf-8

import bisect
from typing import List


class Solution:
    def _find_target(self, nums: List[int], target: int, start: int,
                     end: int) -> int:
        pos = bisect.bisect_left(nums, target, start, end)
        if pos == end or nums[pos] != target:
            return -1
        return pos

    def _find_pivot(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                if mid > 0 and nums[mid] < nums[mid - 1]:
                    return mid
                right = mid - 1
        return left

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if nums[0] <= nums[-1]:
            return self._find_target(nums, target, 0, len(nums))
        pivot_idx = self._find_pivot(nums, target)
        if target >= nums[0]:
            return self._find_target(nums, target, 0, pivot_idx)
        else:
            return self._find_target(nums, target, pivot_idx, len(nums))
