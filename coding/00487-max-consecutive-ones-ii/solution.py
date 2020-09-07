#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = max_cnt = gain = 0
        for v in nums:
            if v == 0:
                gain = 1 + cnt
                cnt = 0
            else:
                cnt += 1
            max_cnt = max(max_cnt, cnt + gain)
        return max_cnt
