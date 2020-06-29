#!/usr/bin/env python3
# encoding: utf-8

# Compute mod and pair things up
# arr: 1, 9, 2, 8, 3, 7
# mod: 1, 4, 2, 3, 3, 2
# mod_to_cnt_map
# check if mod_to_cnt_map[i] == mod_to_cnt_map[k-i] for i = 1..k
# also check if mod_to_cnt_map[0] % 2 == 0

from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_to_cnt_map = {mod: 0 for mod in range(k)}
        for v in arr:
            mod_to_cnt_map[v % k] += 1
        if mod_to_cnt_map[0] % 2 != 0:
            return False
        for mod in range(1, k // 2):
            if mod_to_cnt_map[mod] != mod_to_cnt_map[k-mod]:
                return False
        return True
