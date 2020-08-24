#!/usr/bin/env python3
# encoding: utf-8

import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = bisect.bisect_left(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = bisect.bisect_right(nums, target)
        return [start, end-1]
