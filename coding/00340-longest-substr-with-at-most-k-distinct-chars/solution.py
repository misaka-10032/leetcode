#!/usr/bin/env python3
# encoding: utf-8

from typing import Dict


class Solution:
    def _inc_counter(self, counters: Dict[str, int], char: str):
        cnt = counters.get(char, 0)
        cnt += 1
        counters[char] = cnt

    def _dec_counter(self, counters: Dict[str, int], char: str):
        cnt = counters.get(char, 0)
        cnt -= 1
        if cnt > 0:
            counters[char] = cnt
        else:
            assert cnt == 0
            counters.pop(char)

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        # start and end defines a window of s[start:end]
        start = end = 0
        counters = {}
        max_len = 0
        while end < len(s):
            self._inc_counter(counters, s[end])
            end += 1
            while len(counters) > k:
                self._dec_counter(counters, s[start])
                start += 1
            max_len = max(max_len, end - start)
        return max_len
