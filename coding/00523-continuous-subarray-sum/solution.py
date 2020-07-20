#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def safe_mod(self, v: int, k: int) -> int:
        return v % k if k else v

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        k = abs(k)
        # sum(nums[:i]) % k
        prev_sum_mod = None
        sum_mod = 0
        comp_mods = set()
        for v in nums:
            prev_sum_mod = sum_mod
            sum_mod = self.safe_mod(sum_mod + v, k)
            complement = self.safe_mod(-sum_mod, k)
            if complement in comp_mods:
                return True
            comp_mods.add(self.safe_mod(-prev_sum_mod, k))
        return False
