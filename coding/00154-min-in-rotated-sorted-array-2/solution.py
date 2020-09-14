#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def _tighten(
            self, nums: List[int], left: int, right: int
    ) -> int:
        while left < right and nums[left] == nums[right]:
            right -= 1
        return right

    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        while left < right:
            right = self._tighten(nums, left, right)
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right + 1) // 2
            mid_left = self._tighten(nums, left, mid - 1)
            if nums[left] > nums[mid_left]:
                right = mid_left
                continue

            right = self._tighten(nums, mid, right)
            if nums[mid] > nums[right]:
                left = mid
                continue

            return nums[mid]

        return nums[left]
