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
            if nums[left] <= target <= nums[mid - 1]:
                return self._find_target(nums, target, left, mid - 1)
            if nums[mid] <= target <= nums[right]:
                return self._find_target(nums, target, mid, right)
            if nums[mid] > nums[right]:
                # Pivot is on the right range. The previous conditions
                # failing means the target can only fall within this
                # "pivot" range.
                left = mid
            else:
                if mid > 0 and nums[mid] < nums[mid - 1]:
                    # `mid` is pivot. Both ranges are ascending. However,
                    # If the previous two condition fails, it means the
                    # target cannot exist in this array.
                    return -1
                # Pivot is on the left range. The previous conditions
                # failing means the target can only fall within the "pivot"
                # range.
                right = mid - 1
        return left if nums[left] == target else -1
