#!/usr/bin/env python3
# encoding: utf-8

import bisect
from typing import List


class Solution:
    def _find_target(self, nums: List[int], target: int, left: int,
                     right: int) -> int:
        p = bisect.bisect_left(nums, target, left, right + 1)
        if p == right + 1 or nums[p] != target:
            return -1
        return p

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            for c in (left, mid - 1, mid, right):
                if nums[c] == target:
                    return c
            if nums[left] < target < nums[mid - 1]:
                return self._find_target(nums, target, left, mid - 1)
            if nums[mid] < target < nums[right]:
                return self._find_target(nums, target, mid, right)
            if nums[left] > nums[mid - 1]:
                if target > nums[left] or target < nums[mid - 1]:
                    right = mid - 1
                    continue
            if nums[mid] > nums[right]:
                if target > nums[mid] or target < nums[right]:
                    left = mid
                    continue
            return -1
        return left if nums[left] == target else -1
