#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        val_cnt_pairs = list(collections.Counter(nums).items())
        result = []
        def _search(i: int, comb: List[int]):
            if i == len(val_cnt_pairs):
                result.append(comb[:])
                return
            val, cnt = val_cnt_pairs[i]
            for _ in range(cnt+1):
                _search(i+1, comb)
                comb.append(val)
            for _ in range(cnt+1):
                comb.pop()
        _search(0, [])
        return result
