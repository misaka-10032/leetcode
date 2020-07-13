#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        prev_sum = 0
        cnt = 0
        sum_to_cnt_map = {0: 1}
        for i in range(n):
            new_sum = prev_sum + nums[i]
            complement = new_sum - k
            cnt += sum_to_cnt_map.get(complement, 0)
            # Do the update after the global cnt update to avoid double counting.
            sum_to_cnt_map[new_sum] = 1 + sum_to_cnt_map.get(new_sum, 0)
            prev_sum = new_sum
        return cnt
