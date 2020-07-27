#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def _infer_missing_cnt(self, nums: List[int], right: int) -> int:
        assert right < len(nums)
        if right == 0:
            return 0
        existing_cnt = right - 1
        # If all were missing between (0, right), there would be so many numbers missing.
        missing_cnt_if_all_were_missing = nums[right] - nums[0] - 1
        # However, some numbers exist in-between.
        return missing_cnt_if_all_were_missing - existing_cnt

    def missingElement(self, nums: List[int], k: int) -> int:
        left = 0
        # Insert a pseudo element nums[-1]+k+1 at the last.
        right = len(nums)
        # Left and right defines the index range within which the missing number
        # may appear.
        while left < right - 1:
            mid = (left + right) // 2
            missing_cnt = self._infer_missing_cnt(nums, mid)
            if k <= missing_cnt:
                right = mid
            else:
                left = mid
        assert left == right - 1
        missing_cnt_at_left = self._infer_missing_cnt(nums, left)
        more_missing_cnt_after_left = k - missing_cnt_at_left
        return nums[left] + more_missing_cnt_after_left
