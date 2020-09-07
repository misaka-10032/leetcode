#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_cnt = cnt = 0
        for v in nums:
            if v == 0:
                cnt = 0
            else:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
        return max_cnt
