#!/usr/bin/env python3
# encoding: utf-8

from typing import Dict, List


class Solution:
    def safe_inc(self, char: str, residual_map: Dict[str, int]):
        residual = residual_map.get(char, 0)
        if residual == -1:
            residual_map.pop(char)
        else:
            residual_map[char] = residual + 1

    def safe_dec(self, char: str, residual_map: Dict[str, int]):
        residual = residual_map.get(char, 0)
        if residual == 1:
            residual_map.pop(char)
        else:
            residual_map[char] = residual - 1

    def findAnagrams(self, s: str, p: str) -> List[int]:
        residual_map = {}
        for c in p:
            self.safe_inc(c, residual_map)
        result = []
        for right_idx in range(len(s)):
            # Including a new char can cancel out some residual, so we
            # decrement the counter.
            self.safe_dec(s[right_idx], residual_map)
            left_idx = right_idx - len(p)
            if left_idx >= 0:
                # Excluding a char can add it back to residual.
                self.safe_inc(s[left_idx], residual_map)
            if not residual_map:
                result.append(left_idx + 1)
        return result
