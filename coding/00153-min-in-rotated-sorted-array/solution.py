#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[left] > nums[mid - 1]:
                right = mid - 1
                continue
            if nums[mid] > nums[right]:
                left = mid
                continue
            if nums[left] < nums[right]:
                return nums[left]
            else:
                assert nums[mid] < nums[mid - 1]
                return nums[mid]
        return nums[left]
