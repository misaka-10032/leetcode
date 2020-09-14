#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def _search(i: int, comb: List[int]):
            if i == len(nums):
                result.append(comb[:])
                return
            _search(i+1, comb)
            comb.append(nums[i])
            _search(i+1, comb)
            comb.pop()
        _search(0, [])
        return result
