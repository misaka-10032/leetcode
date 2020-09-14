#!/usr/bin/env python3
# encoding: utf-8

import bisect
from typing import List


class Solution:
    def _tighten(self, nums: List[int], left: int, right: int) -> int:
        while left < right and nums[left] == nums[right]:
            right -= 1
        return right

    def _find_target(self, nums: List[int], left: int, right: int, target: int) -> bool:
        p = bisect.bisect_left(nums, target, left, right + 1)
        return p <= right and nums[p] == target

    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left = 0
        right = len(nums) - 1
        while left < right:
            right = self._tighten(nums, left, right)
            if nums[left] < nums[right]:
                return self._find_target(nums, left, right, target)

            mid = (left + right + 1) // 2
            mid_left = self._tighten(nums, left, mid - 1)
            for c in (left, mid_left):
                if nums[c] == target:
                    return True
            if nums[left] < target < nums[mid_left]:
                return self._find_target(nums, left, mid_left, target)
            if nums[left] > nums[mid_left]:
                if target > nums[left] or target < nums[mid_left]:
                    right = mid_left
                    continue

            right = self._tighten(nums, mid, right)
            for c in (mid, right):
                if nums[c] == target:
                    return True
            if nums[mid] < target < nums[right]:
                return self._find_target(nums, mid, right, target)
            if nums[mid] > nums[right]:
                if target > nums[mid] or target < nums[right]:
                    left = mid
                    continue

            return False
        return nums[left] == target
